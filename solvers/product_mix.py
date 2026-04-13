"""
Product Mix Optimizer — TOC Throughput Accounting with OR-Tools LP

Maximizes total throughput (T) subject to constraint capacity.
Uses Linear Programming to find optimal product mix when multiple
products compete for limited constraint time.

Usage:
    python solvers/product_mix.py --data products.json
    python solvers/product_mix.py --example

Input JSON format:
{
  "constraint": {
    "name": "Painting Station",
    "capacity_minutes": 480
  },
  "products": [
    {
      "name": "Product A",
      "price": 100,
      "tvc": 30,
      "constraint_minutes": 15,
      "max_demand": 50
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
    from ortools.linear_solver import pywraplp
except ImportError:
    print("ERROR: OR-Tools not installed. Run: pip install ortools")
    sys.exit(1)


def solve_product_mix(data: dict) -> dict:
    """
    Solve the TOC product mix problem using Linear Programming.

    The objective is to maximize total Throughput (T = Revenue - TVC)
    subject to:
    - Constraint capacity (total constraint time <= available)
    - Maximum demand per product
    - Non-negativity

    Returns dict with solution details.
    """
    constraint = data["constraint"]
    products = data["products"]

    # Create solver
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return {"error": "Could not create solver"}

    # Decision variables: quantity of each product
    variables = {}
    for p in products:
        name = p["name"]
        max_qty = p.get("max_demand", solver.infinity())
        variables[name] = solver.NumVar(0, max_qty, name)

    # Constraint: total constraint time <= capacity
    constraint_expr = solver.Constraint(0, constraint["capacity_minutes"])
    for p in products:
        constraint_expr.SetCoefficient(
            variables[p["name"]], p["constraint_minutes"]
        )

    # Additional resource constraints (if any)
    for rc in data.get("resources", []):
        rc_constraint = solver.Constraint(0, rc["capacity"])
        for p in products:
            usage = rc.get("usage", {}).get(p["name"], 0)
            if usage > 0:
                rc_constraint.SetCoefficient(variables[p["name"]], usage)

    # Objective: maximize total throughput
    objective = solver.Objective()
    for p in products:
        throughput_per_unit = p["price"] - p["tvc"]
        objective.SetCoefficient(variables[p["name"]], throughput_per_unit)
    objective.SetMaximization()

    # Solve
    status = solver.Solve()

    if status != pywraplp.Solver.OPTIMAL:
        return {"error": f"No optimal solution found (status: {status})"}

    # Build results
    results = {
        "status": "OPTIMAL",
        "total_throughput": objective.Value(),
        "constraint_name": constraint["name"],
        "constraint_capacity": constraint["capacity_minutes"],
        "constraint_used": 0,
        "products": [],
    }

    for p in products:
        name = p["name"]
        qty = variables[name].solution_value()
        t_per_unit = p["price"] - p["tvc"]
        t_per_cu = t_per_unit / p["constraint_minutes"] if p["constraint_minutes"] > 0 else float("inf")
        constraint_used = qty * p["constraint_minutes"]
        results["constraint_used"] += constraint_used

        results["products"].append({
            "name": name,
            "quantity": round(qty, 1),
            "throughput_per_unit": t_per_unit,
            "throughput_per_constraint_unit": round(t_per_cu, 2),
            "total_throughput": round(qty * t_per_unit, 2),
            "constraint_minutes_used": round(constraint_used, 1),
            "demand_limit": p.get("max_demand"),
        })

    # Sort by T/CU (TOC ranking)
    results["products"].sort(
        key=lambda x: x["throughput_per_constraint_unit"], reverse=True
    )

    results["constraint_used"] = round(results["constraint_used"], 1)
    cap = constraint["capacity_minutes"]
    results["constraint_utilization"] = round(
        results["constraint_used"] / cap * 100, 1
    ) if cap > 0 else 0

    return results


def format_results(results: dict) -> str:
    """Format results as readable text."""
    if "error" in results:
        return f"ERROR: {results['error']}"

    lines = []
    lines.append("=" * 60)
    lines.append("  PRODUCT MIX OPTIMIZATION — TOC Throughput Maximization")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"  Constraint: {results['constraint_name']}")
    lines.append(f"  Capacity: {results['constraint_capacity']} min")
    lines.append(f"  Used: {results['constraint_used']} min ({results['constraint_utilization']}%)")
    lines.append("")
    lines.append("-" * 60)
    lines.append(f"  {'Product':<20} {'Qty':>6} {'T/unit':>8} {'T/CU':>8} {'Total T':>10}")
    lines.append("-" * 60)

    for p in results["products"]:
        lines.append(
            f"  {p['name']:<20} {p['quantity']:>6.0f} "
            f"${p['throughput_per_unit']:>6.0f} "
            f"${p['throughput_per_constraint_unit']:>6.2f} "
            f"${p['total_throughput']:>9.0f}"
        )

    lines.append("-" * 60)
    lines.append(f"  {'TOTAL THROUGHPUT':>46} ${results['total_throughput']:>9.0f}")
    lines.append("=" * 60)
    lines.append("")
    lines.append("  T/CU = Throughput per Constraint Unit (higher = priority)")
    lines.append("  Products sorted by T/CU — TOC optimal sequence")

    return "\n".join(lines)


def create_example() -> dict:
    """Create example data for demonstration."""
    return {
        "constraint": {
            "name": "Painting Station",
            "capacity_minutes": 480
        },
        "products": [
            {
                "name": "Standard Widget",
                "price": 100,
                "tvc": 30,
                "constraint_minutes": 15,
                "max_demand": 40
            },
            {
                "name": "Premium Widget",
                "price": 180,
                "tvc": 60,
                "constraint_minutes": 30,
                "max_demand": 20
            },
            {
                "name": "Economy Widget",
                "price": 50,
                "tvc": 15,
                "constraint_minutes": 8,
                "max_demand": 60
            },
            {
                "name": "Custom Widget",
                "price": 250,
                "tvc": 100,
                "constraint_minutes": 45,
                "max_demand": 10
            },
        ]
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TOC Product Mix Optimizer")
    parser.add_argument("--data", help="JSON file with product data")
    parser.add_argument("--example", action="store_true", help="Run with example data")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if args.data:
        data = json.loads(Path(args.data).read_text(encoding="utf-8"))
    elif args.example:
        data = create_example()
    else:
        print("Usage: python product_mix.py --data products.json")
        print("       python product_mix.py --example")
        sys.exit(1)

    results = solve_product_mix(data)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_results(results))
