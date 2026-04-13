"""
DBR Scheduler — Drum-Buffer-Rope Scheduling with OR-Tools CP-SAT

Schedules jobs through a multi-stage process, respecting the constraint
(drum) capacity, maintaining buffers, and controlling work release (rope).

Usage:
    python solvers/dbr_scheduler.py --data jobs.json
    python solvers/dbr_scheduler.py --example

Input JSON format:
{
  "stages": [
    {"name": "Cutting", "capacity_per_hour": 20},
    {"name": "Welding", "capacity_per_hour": 15},
    {"name": "Painting", "capacity_per_hour": 10, "is_drum": true},
    {"name": "Assembly", "capacity_per_hour": 25}
  ],
  "jobs": [
    {"name": "Job-001", "quantity": 5, "due_date": 48, "priority": 1},
    {"name": "Job-002", "quantity": 8, "due_date": 72, "priority": 2}
  ],
  "buffer_hours": 4,
  "horizon_hours": 120
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


def solve_dbr_schedule(data: dict) -> dict:
    """
    Solve DBR scheduling using Constraint Programming (CP-SAT).

    Minimizes total tardiness (late deliveries) while respecting:
    - Stage sequence (each job goes through stages in order)
    - Constraint (drum) capacity limits
    - Buffer time before the drum
    - Job priorities
    """
    stages = data["stages"]
    jobs = data["jobs"]
    buffer_hours = data.get("buffer_hours", 4)
    horizon = data.get("horizon_hours", 168)  # 1 week default

    # Find drum (constraint) — auto-detect if not marked
    drum_candidates = [i for i, s in enumerate(stages) if s.get("is_drum", False)]
    if drum_candidates:
        drum_idx = drum_candidates[0]
    else:
        # Auto-select: lowest capacity stage is the drum
        drum_idx = min(range(len(stages)), key=lambda i: stages[i]["capacity_per_hour"])
    drum = stages[drum_idx]

    model = cp_model.CpModel()

    # Variables: start time and end time for each job at each stage
    # NOTE: CP-SAT requires integer variables. All times are scaled x10
    # (0.1h precision) then divided by 10 in output. E.g., 4.5h -> 45 -> display 4.5h
    SCALE = 10
    starts = {}
    ends = {}
    intervals = {}

    for j_idx, job in enumerate(jobs):
        for s_idx, stage in enumerate(stages):
            proc_time = max(1, round(job["quantity"] / stage["capacity_per_hour"] * SCALE))

            start_var = model.NewIntVar(0, horizon * 10, f"start_j{j_idx}_s{s_idx}")
            end_var = model.NewIntVar(0, horizon * 10, f"end_j{j_idx}_s{s_idx}")
            interval_var = model.NewIntervalVar(
                start_var, proc_time, end_var, f"interval_j{j_idx}_s{s_idx}"
            )

            starts[(j_idx, s_idx)] = start_var
            ends[(j_idx, s_idx)] = end_var
            intervals[(j_idx, s_idx)] = interval_var

            # Stage sequence: job must finish stage s before starting s+1
            if s_idx > 0:
                model.Add(starts[(j_idx, s_idx)] >= ends[(j_idx, s_idx - 1)])

            # Buffer before drum: must have buffer_hours gap before drum stage
            if s_idx == drum_idx and s_idx > 0:
                model.Add(
                    starts[(j_idx, s_idx)] >= ends[(j_idx, s_idx - 1)] + buffer_hours * 10
                )

    # No overlap at the drum (constraint is the bottleneck)
    drum_intervals = [intervals[(j, drum_idx)] for j in range(len(jobs))]
    model.AddNoOverlap(drum_intervals)

    # Also no overlap at other stages (realistic: one job at a time per stage)
    for s_idx in range(len(stages)):
        if s_idx != drum_idx:
            stage_intervals = [intervals[(j, s_idx)] for j in range(len(jobs))]
            model.AddNoOverlap(stage_intervals)

    # Tardiness variables
    last_stage = len(stages) - 1
    tardiness_vars = []
    for j_idx, job in enumerate(jobs):
        due = job["due_date"] * 10
        tard = model.NewIntVar(0, horizon * 10, f"tard_j{j_idx}")
        model.Add(tard >= ends[(j_idx, last_stage)] - due)
        model.Add(tard >= 0)
        tardiness_vars.append(tard)

    # Objective: minimize weighted tardiness (priority × tardiness)
    objective_terms = []
    for j_idx, job in enumerate(jobs):
        weight = job.get("priority", 1)
        objective_terms.append(tardiness_vars[j_idx] * weight)
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
        "drum": drum["name"],
        "buffer_hours": buffer_hours,
        "schedule": [],
        "summary": {
            "total_tardiness_hours": 0,
            "on_time_jobs": 0,
            "late_jobs": 0,
            "drum_utilization": 0,
        }
    }

    drum_busy = 0
    for j_idx, job in enumerate(jobs):
        job_schedule = {
            "job": job["name"],
            "quantity": job["quantity"],
            "due_date": job["due_date"],
            "priority": job.get("priority", 1),
            "stages": [],
        }

        for s_idx, stage in enumerate(stages):
            start_val = solver.Value(starts[(j_idx, s_idx)]) / 10
            end_val = solver.Value(ends[(j_idx, s_idx)]) / 10
            job_schedule["stages"].append({
                "stage": stage["name"],
                "start": round(start_val, 1),
                "end": round(end_val, 1),
                "is_drum": s_idx == drum_idx,
            })
            if s_idx == drum_idx:
                drum_busy += (end_val - start_val)

        completion = solver.Value(ends[(j_idx, last_stage)]) / 10
        tard = solver.Value(tardiness_vars[j_idx]) / 10
        job_schedule["completion"] = round(completion, 1)
        job_schedule["tardiness"] = round(tard, 1)
        job_schedule["on_time"] = tard < 0.1

        if job_schedule["on_time"]:
            results["summary"]["on_time_jobs"] += 1
        else:
            results["summary"]["late_jobs"] += 1
        results["summary"]["total_tardiness_hours"] += tard

        results["schedule"].append(job_schedule)

    # Sort by drum start time (rope release order)
    results["schedule"].sort(
        key=lambda x: next(s["start"] for s in x["stages"] if s["is_drum"])
    )

    makespan = max(j["completion"] for j in results["schedule"])
    results["summary"]["makespan_hours"] = round(makespan, 1)
    results["summary"]["drum_utilization"] = round(drum_busy / horizon * 100, 1) if horizon > 0 else 0
    results["summary"]["total_tardiness_hours"] = round(results["summary"]["total_tardiness_hours"], 1)

    return results


def format_results(results: dict) -> str:
    """Format results as readable text."""
    if "error" in results:
        return f"ERROR: {results['error']}"

    lines = []
    lines.append("=" * 70)
    lines.append("  DBR SCHEDULE — Drum-Buffer-Rope Optimization")
    lines.append("=" * 70)
    lines.append(f"  Drum (constraint): {results['drum']}")
    lines.append(f"  Buffer: {results['buffer_hours']} hours before drum")
    lines.append(f"  Status: {results['status']}")
    lines.append("")

    # Gantt-style schedule
    lines.append("-" * 70)
    lines.append("  SCHEDULE (sorted by drum start — this is the ROPE release order):")
    lines.append("-" * 70)

    for job in results["schedule"]:
        status = "ON TIME" if job["on_time"] else f"LATE +{job['tardiness']}h"
        lines.append(f"\n  {job['job']} (qty:{job['quantity']}, due:{job['due_date']}h) — {status}")
        for stage in job["stages"]:
            marker = " [DRUM]" if stage["is_drum"] else ""
            lines.append(f"    {stage['stage']:<20} {stage['start']:>6.1f}h — {stage['end']:>6.1f}h{marker}")

    lines.append("")
    lines.append("-" * 70)
    lines.append("  SUMMARY:")
    s = results["summary"]
    lines.append(f"    Makespan: {s['makespan_hours']}h")
    lines.append(f"    On-time: {s['on_time_jobs']} jobs | Late: {s['late_jobs']} jobs")
    lines.append(f"    Total tardiness: {s['total_tardiness_hours']}h")
    lines.append(f"    Drum utilization: {s['drum_utilization']}%")
    lines.append("=" * 70)

    return "\n".join(lines)


def create_example() -> dict:
    """Create example data."""
    return {
        "stages": [
            {"name": "Cutting", "capacity_per_hour": 20},
            {"name": "Welding", "capacity_per_hour": 15},
            {"name": "Painting", "capacity_per_hour": 10, "is_drum": True},
            {"name": "Assembly", "capacity_per_hour": 25},
        ],
        "jobs": [
            {"name": "Job-001", "quantity": 12, "due_date": 24, "priority": 3},
            {"name": "Job-002", "quantity": 8, "due_date": 36, "priority": 2},
            {"name": "Job-003", "quantity": 20, "due_date": 48, "priority": 1},
            {"name": "Job-004", "quantity": 5, "due_date": 30, "priority": 3},
            {"name": "Job-005", "quantity": 15, "due_date": 60, "priority": 1},
        ],
        "buffer_hours": 4,
        "horizon_hours": 120,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TOC DBR Scheduler")
    parser.add_argument("--data", help="JSON file with job data")
    parser.add_argument("--example", action="store_true", help="Run with example data")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if args.data:
        data = json.loads(Path(args.data).read_text(encoding="utf-8"))
    elif args.example:
        data = create_example()
    else:
        print("Usage: python dbr_scheduler.py --data jobs.json")
        print("       python dbr_scheduler.py --example")
        sys.exit(1)

    results = solve_dbr_schedule(data)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_results(results))
