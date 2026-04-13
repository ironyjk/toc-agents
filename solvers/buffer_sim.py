"""
Buffer Sizing Simulator — Monte Carlo Simulation for TOC Buffers

Determines optimal buffer sizes for DBR constraint buffers and
CCPM project buffers using Monte Carlo simulation.

Usage:
    python solvers/buffer_sim.py --data buffer_config.json
    python solvers/buffer_sim.py --example

Input JSON format:
{
  "tasks": [
    {"name": "Task A", "optimistic": 3, "most_likely": 5, "pessimistic": 12},
    {"name": "Task B", "optimistic": 2, "most_likely": 4, "pessimistic": 8}
  ],
  "target_confidence": 0.95,
  "simulations": 10000
}

Co-created by @ironyjk x Claude Code
"""

import json
import sys
import argparse
import math
from pathlib import Path

try:
    import numpy as np
except ImportError:
    print("ERROR: numpy not installed. Run: pip install numpy")
    sys.exit(1)


def triangular_sample(optimistic, most_likely, pessimistic, size=1):
    """Sample from triangular distribution (PERT-like)."""
    return np.random.triangular(optimistic, most_likely, pessimistic, size)


def beta_pert_sample(optimistic, most_likely, pessimistic, size=1, lambd=4):
    """Sample from Beta-PERT distribution (better than triangular for project estimates)."""
    if pessimistic <= optimistic:
        return np.full(size, most_likely)

    mean = (optimistic + lambd * most_likely + pessimistic) / (lambd + 2)

    # Guard against degenerate cases where most_likely == mean
    denom1 = (most_likely - mean) * (pessimistic - optimistic)
    denom2 = mean - optimistic
    if abs(denom1) < 1e-10 or abs(denom2) < 1e-10:
        # Fall back to triangular distribution for edge cases
        return np.random.triangular(optimistic, most_likely, pessimistic, size)

    # Beta distribution parameters
    alpha1 = ((mean - optimistic) * (2 * most_likely - optimistic - pessimistic)) / denom1
    alpha2 = alpha1 * (pessimistic - mean) / denom2

    if alpha1 <= 0 or alpha2 <= 0:
        return np.random.triangular(optimistic, most_likely, pessimistic, size)

    samples = np.random.beta(alpha1, alpha2, size)
    return optimistic + samples * (pessimistic - optimistic)


def simulate_buffers(data: dict) -> dict:
    """
    Run Monte Carlo simulation to determine optimal buffer sizes.

    For each simulation run:
    1. Sample task durations from Beta-PERT distribution
    2. Calculate total chain duration
    3. Repeat N times
    4. Determine buffer at target confidence level
    """
    tasks = data["tasks"]
    target_conf = data.get("target_confidence", 0.95)
    n_sims = data.get("simulations", 10000)

    np.random.seed(data.get("seed", None))

    # Aggressive estimates (CCPM: 50% of safe/pessimistic estimate)
    aggressive_total = sum(t["pessimistic"] / 2 for t in tasks)

    # Simulate total duration
    total_durations = np.zeros(n_sims)
    task_durations_all = {}

    for task in tasks:
        samples = beta_pert_sample(
            task["optimistic"],
            task["most_likely"],
            task["pessimistic"],
            size=n_sims,
        )
        task_durations_all[task["name"]] = samples
        total_durations += samples

    # Statistics
    mean_duration = float(np.mean(total_durations))
    median_duration = float(np.median(total_durations))
    std_duration = float(np.std(total_durations))
    p50 = float(np.percentile(total_durations, 50))
    p75 = float(np.percentile(total_durations, 75))
    p90 = float(np.percentile(total_durations, 90))
    p95 = float(np.percentile(total_durations, 95))
    p99 = float(np.percentile(total_durations, 99))
    target_duration = float(np.percentile(total_durations, target_conf * 100))

    # Buffer calculations
    # Method 1: Cut-and-Paste (Goldratt) — 50% of safe chain
    safe_total = sum(t["pessimistic"] for t in tasks)
    goldratt_buffer = safe_total * 0.5

    # Method 2: Root Sum of Squares (RSS) — statistical
    variances = []
    for task in tasks:
        safe = task["pessimistic"]
        aggressive = task["pessimistic"] / 2
        safety = safe - aggressive
        variances.append(safety ** 2)
    rss_buffer = math.sqrt(sum(variances))

    # Method 3: Monte Carlo — simulation-based
    mc_buffer = target_duration - aggressive_total

    # Per-task analysis
    task_analysis = []
    for task in tasks:
        samples = task_durations_all[task["name"]]
        aggressive = task["pessimistic"] / 2
        task_analysis.append({
            "name": task["name"],
            "optimistic": task["optimistic"],
            "most_likely": task["most_likely"],
            "pessimistic": task["pessimistic"],
            "aggressive_estimate": round(aggressive, 1),
            "sim_mean": round(float(np.mean(samples)), 1),
            "sim_std": round(float(np.std(samples)), 1),
            "sim_p95": round(float(np.percentile(samples, 95)), 1),
            "safety_consumed": round(float(np.mean(samples)) - aggressive, 1),
        })

    return {
        "simulations": n_sims,
        "target_confidence": target_conf,
        "chain_analysis": {
            "aggressive_total": round(aggressive_total, 1),
            "safe_total": round(safe_total, 1),
            "sim_mean": round(mean_duration, 1),
            "sim_median": round(median_duration, 1),
            "sim_std": round(std_duration, 1),
        },
        "percentiles": {
            "p50": round(p50, 1),
            "p75": round(p75, 1),
            "p90": round(p90, 1),
            "p95": round(p95, 1),
            "p99": round(p99, 1),
        },
        "buffer_methods": {
            "goldratt_cut_and_paste": round(goldratt_buffer, 1),
            "root_sum_of_squares": round(rss_buffer, 1),
            "monte_carlo": round(mc_buffer, 1),
        },
        "recommendation": {
            "method": "monte_carlo",
            "buffer_size": round(mc_buffer, 1),
            "total_with_buffer": round(aggressive_total + mc_buffer, 1),
            "confidence": target_conf,
        },
        "task_analysis": task_analysis,
    }


def format_results(results: dict) -> str:
    """Format results as readable text."""
    lines = []
    lines.append("=" * 65)
    lines.append("  BUFFER SIZING — Monte Carlo Simulation")
    lines.append("=" * 65)
    lines.append(f"  Simulations: {results['simulations']:,}")
    lines.append(f"  Target confidence: {results['target_confidence']*100:.0f}%")
    lines.append("")

    ca = results["chain_analysis"]
    lines.append("  CHAIN DURATION:")
    lines.append(f"    Aggressive (50% cut): {ca['aggressive_total']} days")
    lines.append(f"    Safe (pessimistic):   {ca['safe_total']} days")
    lines.append(f"    Simulated mean:       {ca['sim_mean']} days (+/- {ca['sim_std']})")
    lines.append("")

    p = results["percentiles"]
    lines.append("  PERCENTILES:")
    lines.append(f"    P50: {p['p50']}d | P75: {p['p75']}d | P90: {p['p90']}d | P95: {p['p95']}d | P99: {p['p99']}d")
    lines.append("")

    bm = results["buffer_methods"]
    lines.append("  BUFFER METHODS COMPARED:")
    lines.append(f"    Goldratt (50% cut):       {bm['goldratt_cut_and_paste']} days")
    lines.append(f"    RSS (statistical):        {bm['root_sum_of_squares']} days")
    lines.append(f"    Monte Carlo (simulated):  {bm['monte_carlo']} days")
    lines.append("")

    rec = results["recommendation"]
    lines.append("-" * 65)
    lines.append(f"  RECOMMENDATION: Buffer = {rec['buffer_size']} days")
    lines.append(f"  Total (aggressive + buffer): {rec['total_with_buffer']} days")
    lines.append(f"  Confidence: {rec['confidence']*100:.0f}%")
    lines.append("-" * 65)

    lines.append("")
    lines.append("  PER-TASK ANALYSIS:")
    lines.append(f"    {'Task':<20} {'Aggr':>5} {'Mean':>5} {'P95':>5} {'Safety used':>12}")
    lines.append(f"    {'-'*50}")
    for t in results["task_analysis"]:
        lines.append(
            f"    {t['name']:<20} {t['aggressive_estimate']:>4.0f}d "
            f"{t['sim_mean']:>4.0f}d {t['sim_p95']:>4.0f}d "
            f"{t['safety_consumed']:>+10.1f}d"
        )

    lines.append("=" * 65)
    return "\n".join(lines)


def create_example() -> dict:
    """Create example data."""
    return {
        "tasks": [
            {"name": "Requirements", "optimistic": 3, "most_likely": 5, "pessimistic": 12},
            {"name": "Design", "optimistic": 5, "most_likely": 8, "pessimistic": 20},
            {"name": "Backend Dev", "optimistic": 8, "most_likely": 14, "pessimistic": 30},
            {"name": "Frontend Dev", "optimistic": 6, "most_likely": 10, "pessimistic": 22},
            {"name": "Integration", "optimistic": 3, "most_likely": 6, "pessimistic": 15},
            {"name": "Testing", "optimistic": 4, "most_likely": 7, "pessimistic": 16},
        ],
        "target_confidence": 0.95,
        "simulations": 10000,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TOC Buffer Sizing Simulator")
    parser.add_argument("--data", help="JSON file with task estimates")
    parser.add_argument("--example", action="store_true", help="Run with example data")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if args.data:
        data = json.loads(Path(args.data).read_text(encoding="utf-8"))
    elif args.example:
        data = create_example()
    else:
        print("Usage: python buffer_sim.py --data config.json")
        print("       python buffer_sim.py --example")
        sys.exit(1)

    results = simulate_buffers(data)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_results(results))
