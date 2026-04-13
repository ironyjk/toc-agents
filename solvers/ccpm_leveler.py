"""
CCPM Resource Leveler — Critical Chain Project Management with OR-Tools

Schedules multiple projects sharing a drum resource, applies CCPM principles:
- Cut task estimates by 50%
- Add project buffers (50% of critical chain)
- Stagger projects by drum resource
- No multitasking — one task per resource at a time

Usage:
    python solvers/ccpm_leveler.py --data projects.json
    python solvers/ccpm_leveler.py --example

Input JSON format:
{
  "resources": ["Alice", "Bob", "Charlie"],
  "drum_resource": "Bob",
  "projects": [
    {
      "name": "Project Alpha",
      "tasks": [
        {"name": "Design", "resource": "Alice", "safe_estimate_days": 10, "depends_on": []},
        {"name": "Build", "resource": "Bob", "safe_estimate_days": 8, "depends_on": ["Design"]},
        {"name": "Test", "resource": "Charlie", "safe_estimate_days": 6, "depends_on": ["Build"]}
      ],
      "deadline_day": 30
    }
  ]
}

Co-created by @ironyjk x Claude Code
"""

import json
import sys
import argparse
from pathlib import Path

try:
    from ortools.sat.python import cp_model
except ImportError:
    print("ERROR: OR-Tools not installed. Run: pip install ortools")
    sys.exit(1)


def solve_ccpm(data: dict) -> dict:
    """
    Solve multi-project CCPM scheduling.

    CCPM principles applied:
    1. Task durations cut to 50% of safe estimate
    2. No multitasking: one task per resource at a time
    3. Projects staggered by drum resource availability
    4. Project buffer = 50% of critical chain length
    """
    resources = data["resources"]
    drum_resource = data["drum_resource"]
    projects = data["projects"]
    horizon = data.get("horizon_days", 200)

    model = cp_model.CpModel()

    # Task variables
    starts = {}
    ends = {}
    intervals = {}
    task_lookup = {}  # (proj_idx, task_name) -> task dict

    # Pass 1: Create all variables first
    for p_idx, project in enumerate(projects):
        for task in project["tasks"]:
            key = (p_idx, task["name"])
            task_lookup[key] = task

            # CCPM: cut to 50% of safe estimate
            aggressive_duration = max(1, task["safe_estimate_days"] // 2)

            s = model.NewIntVar(0, horizon, f"s_p{p_idx}_{task['name']}")
            e = model.NewIntVar(0, horizon, f"e_p{p_idx}_{task['name']}")
            iv = model.NewIntervalVar(s, aggressive_duration, e, f"iv_p{p_idx}_{task['name']}")

            starts[key] = s
            ends[key] = e
            intervals[key] = iv

    # Pass 2: Add dependency constraints (all variables now exist)
    for p_idx, project in enumerate(projects):
        for task in project["tasks"]:
            key = (p_idx, task["name"])
            for dep_name in task.get("depends_on", []):
                dep_key = (p_idx, dep_name)
                if dep_key not in ends:
                    raise ValueError(
                        f"Task '{task['name']}' depends on '{dep_name}' "
                        f"which does not exist in project '{project['name']}'"
                    )
                model.Add(starts[key] >= ends[dep_key])

    # No multitasking: one task per resource at a time (across ALL projects)
    for resource in resources:
        resource_intervals = []
        for p_idx, project in enumerate(projects):
            for task in project["tasks"]:
                if task["resource"] == resource:
                    resource_intervals.append(intervals[(p_idx, task["name"])])
        if resource_intervals:
            model.AddNoOverlap(resource_intervals)

    # Project completion times
    project_completions = {}
    for p_idx, project in enumerate(projects):
        last_tasks = [ends[(p_idx, t["name"])] for t in project["tasks"]]
        comp = model.NewIntVar(0, horizon, f"comp_p{p_idx}")
        model.AddMaxEquality(comp, last_tasks)
        project_completions[p_idx] = comp

    # Objective: minimize total project completion (weighted by deadline urgency)
    objective_terms = []
    for p_idx, project in enumerate(projects):
        deadline = project.get("deadline_day", horizon)
        weight = max(1, horizon - deadline)  # more urgent = higher weight
        objective_terms.append(project_completions[p_idx] * weight)
    model.Minimize(sum(objective_terms))

    # Solve
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 30
    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return {"error": f"No solution found (status: {status})"}

    # Build results
    results = {
        "status": "OPTIMAL" if status == cp_model.OPTIMAL else "FEASIBLE",
        "drum_resource": drum_resource,
        "ccpm_note": "Task durations are 50% of safe estimates. Add project buffer for safety.",
        "projects": [],
    }

    for p_idx, project in enumerate(projects):
        proj_result = {
            "name": project["name"],
            "deadline": project.get("deadline_day"),
            "tasks": [],
            "critical_chain_days": 0,
        }

        max_end = 0
        for task in project["tasks"]:
            key = (p_idx, task["name"])
            s_val = solver.Value(starts[key])
            e_val = solver.Value(ends[key])
            aggressive = max(1, task["safe_estimate_days"] // 2)

            proj_result["tasks"].append({
                "name": task["name"],
                "resource": task["resource"],
                "is_drum": task["resource"] == drum_resource,
                "safe_estimate": task["safe_estimate_days"],
                "aggressive_duration": aggressive,
                "start_day": s_val,
                "end_day": e_val,
            })
            max_end = max(max_end, e_val)

        proj_result["completion_day"] = max_end
        # Critical chain = actual longest path (from solver schedule)
        min_start = min(t["start_day"] for t in proj_result["tasks"])
        cc_length = max_end - min_start
        proj_result["critical_chain_days"] = cc_length
        proj_result["project_buffer_days"] = max(1, cc_length // 2)
        proj_result["buffered_completion"] = max_end + proj_result["project_buffer_days"]

        deadline = project.get("deadline_day", horizon)
        proj_result["on_time"] = proj_result["buffered_completion"] <= deadline
        proj_result["slack"] = deadline - proj_result["buffered_completion"]

        results["projects"].append(proj_result)

    return results


def format_results(results: dict) -> str:
    """Format results as readable text."""
    if "error" in results:
        return f"ERROR: {results['error']}"

    lines = []
    lines.append("=" * 70)
    lines.append("  CCPM SCHEDULE — Critical Chain Project Management")
    lines.append("=" * 70)
    lines.append(f"  Drum resource: {results['drum_resource']}")
    lines.append(f"  Note: {results['ccpm_note']}")
    lines.append("")

    for proj in results["projects"]:
        status = "ON TIME" if proj["on_time"] else f"LATE by {-proj['slack']} days"
        lines.append(f"\n  PROJECT: {proj['name']} (deadline: day {proj['deadline']}) — {status}")
        lines.append(f"  Critical chain: {proj['critical_chain_days']}d | Buffer: {proj['project_buffer_days']}d")
        lines.append(f"  Completion: day {proj['completion_day']} + buffer = day {proj['buffered_completion']}")
        lines.append("")
        lines.append(f"    {'Task':<20} {'Resource':<12} {'Safe':>5} {'Aggr':>5} {'Start':>6} {'End':>6}")
        lines.append(f"    {'-'*56}")

        for t in proj["tasks"]:
            drum_mark = " [DRUM]" if t["is_drum"] else ""
            lines.append(
                f"    {t['name']:<20} {t['resource']:<12} "
                f"{t['safe_estimate']:>4}d {t['aggressive_duration']:>4}d "
                f"{t['start_day']:>5} {t['end_day']:>5}{drum_mark}"
            )

    lines.append("")
    lines.append("=" * 70)
    lines.append("  BUFFER MANAGEMENT:")
    lines.append("    Green (0-33%): Normal | Yellow (34-66%): Monitor | Red (67-100%): Act")
    lines.append("=" * 70)

    return "\n".join(lines)


def create_example() -> dict:
    """Create example multi-project data."""
    return {
        "resources": ["Alice", "Bob", "Charlie", "Diana"],
        "drum_resource": "Bob",
        "projects": [
            {
                "name": "Website Redesign",
                "deadline_day": 40,
                "tasks": [
                    {"name": "Requirements", "resource": "Alice", "safe_estimate_days": 6, "depends_on": []},
                    {"name": "UI Design", "resource": "Diana", "safe_estimate_days": 10, "depends_on": ["Requirements"]},
                    {"name": "Backend", "resource": "Bob", "safe_estimate_days": 14, "depends_on": ["Requirements"]},
                    {"name": "Frontend", "resource": "Charlie", "safe_estimate_days": 12, "depends_on": ["UI Design"]},
                    {"name": "Integration", "resource": "Bob", "safe_estimate_days": 8, "depends_on": ["Backend", "Frontend"]},
                    {"name": "Testing", "resource": "Alice", "safe_estimate_days": 6, "depends_on": ["Integration"]},
                ]
            },
            {
                "name": "Mobile App",
                "deadline_day": 50,
                "tasks": [
                    {"name": "App Design", "resource": "Diana", "safe_estimate_days": 8, "depends_on": []},
                    {"name": "API Layer", "resource": "Bob", "safe_estimate_days": 10, "depends_on": ["App Design"]},
                    {"name": "App Dev", "resource": "Charlie", "safe_estimate_days": 16, "depends_on": ["App Design"]},
                    {"name": "API Integration", "resource": "Bob", "safe_estimate_days": 6, "depends_on": ["API Layer", "App Dev"]},
                    {"name": "QA", "resource": "Alice", "safe_estimate_days": 8, "depends_on": ["API Integration"]},
                ]
            }
        ],
        "horizon_days": 100,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TOC CCPM Resource Leveler")
    parser.add_argument("--data", help="JSON file with project data")
    parser.add_argument("--example", action="store_true", help="Run with example data")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if args.data:
        data = json.loads(Path(args.data).read_text(encoding="utf-8"))
    elif args.example:
        data = create_example()
    else:
        print("Usage: python ccpm_leveler.py --data projects.json")
        print("       python ccpm_leveler.py --example")
        sys.exit(1)

    results = solve_ccpm(data)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_results(results))
