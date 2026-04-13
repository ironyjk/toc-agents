"""
Basic tests for TOC solvers — runs each solver with example data
and verifies output structure and constraints.

Usage:
    python -m pytest solvers/test_solvers.py -v
    python solvers/test_solvers.py  (standalone)
"""

import sys
import json

# Import solvers
from product_mix import solve_product_mix, create_example as pm_example
from dbr_scheduler import solve_dbr_schedule, create_example as dbr_example
from ccpm_leveler import solve_ccpm, create_example as ccpm_example
from buffer_sim import simulate_buffers, create_example as buf_example


def test_product_mix_example():
    """Product mix solver returns optimal solution with correct structure."""
    data = pm_example()
    result = solve_product_mix(data)

    assert result["status"] == "OPTIMAL"
    assert result["total_throughput"] > 0
    assert result["constraint_utilization"] <= 100.1
    assert len(result["products"]) == len(data["products"])

    # T/CU ordering: first product should have highest T/CU
    tcus = [p["throughput_per_constraint_unit"] for p in result["products"]]
    assert tcus == sorted(tcus, reverse=True)

    # No product exceeds max demand
    for p_result in result["products"]:
        orig = next(p for p in data["products"] if p["name"] == p_result["name"])
        if orig.get("max_demand"):
            assert p_result["quantity"] <= orig["max_demand"] + 0.1

    print("  product_mix: PASS")


def test_product_mix_empty():
    """Product mix with no products returns zero throughput."""
    data = {"constraint": {"name": "X", "capacity_minutes": 480}, "products": []}
    result = solve_product_mix(data)
    assert result["status"] == "OPTIMAL"
    assert result["total_throughput"] == 0
    print("  product_mix empty: PASS")


def test_product_mix_zero_capacity():
    """Product mix with zero capacity."""
    data = pm_example()
    data["constraint"]["capacity_minutes"] = 0
    result = solve_product_mix(data)
    # Should still return optimal with 0 throughput (no capacity)
    assert result["status"] == "OPTIMAL"
    assert result["total_throughput"] == 0
    print("  product_mix zero capacity: PASS")


def test_dbr_scheduler_example():
    """DBR scheduler returns feasible schedule."""
    data = dbr_example()
    result = solve_dbr_schedule(data)

    assert result["status"] in ("OPTIMAL", "FEASIBLE")
    assert len(result["schedule"]) == len(data["jobs"])
    assert result["drum"] == "Painting"

    # All jobs have all stages
    for job in result["schedule"]:
        assert len(job["stages"]) == len(data["stages"])
        # Stages are in order (start of stage N+1 >= end of stage N)
        for i in range(1, len(job["stages"])):
            assert job["stages"][i]["start"] >= job["stages"][i-1]["end"] - 0.1

    print("  dbr_scheduler: PASS")


def test_dbr_auto_drum():
    """DBR auto-detects drum when no stage marked is_drum."""
    data = dbr_example()
    for stage in data["stages"]:
        stage.pop("is_drum", None)
    result = solve_dbr_schedule(data)
    assert result["status"] in ("OPTIMAL", "FEASIBLE")
    # Should pick lowest capacity (Painting=10)
    assert result["drum"] == "Painting"
    print("  dbr auto-drum: PASS")


def test_ccpm_example():
    """CCPM leveler returns valid schedule."""
    data = ccpm_example()
    result = solve_ccpm(data)

    assert result["status"] in ("OPTIMAL", "FEASIBLE")
    assert len(result["projects"]) == len(data["projects"])

    for proj in result["projects"]:
        assert proj["critical_chain_days"] > 0
        assert proj["project_buffer_days"] > 0
        assert proj["buffered_completion"] > proj["completion_day"]

        # No task starts before day 0
        for t in proj["tasks"]:
            assert t["start_day"] >= 0

    print("  ccpm_leveler: PASS")


def test_ccpm_dependency_order():
    """CCPM handles out-of-order task definitions correctly."""
    data = {
        "resources": ["A", "B"],
        "drum_resource": "B",
        "projects": [{
            "name": "Test",
            "deadline_day": 50,
            "tasks": [
                # Build depends on Design, but Build is listed first
                {"name": "Build", "resource": "B", "safe_estimate_days": 10, "depends_on": ["Design"]},
                {"name": "Design", "resource": "A", "safe_estimate_days": 6, "depends_on": []},
                {"name": "Test", "resource": "A", "safe_estimate_days": 4, "depends_on": ["Build"]},
            ]
        }],
    }
    result = solve_ccpm(data)
    assert result["status"] in ("OPTIMAL", "FEASIBLE")

    tasks = {t["name"]: t for t in result["projects"][0]["tasks"]}
    # Design must finish before Build starts
    assert tasks["Build"]["start_day"] >= tasks["Design"]["end_day"]
    # Build must finish before Test starts
    assert tasks["Test"]["start_day"] >= tasks["Build"]["end_day"]

    print("  ccpm dependency order: PASS")


def test_ccpm_invalid_dependency():
    """CCPM raises error for nonexistent dependency."""
    data = {
        "resources": ["A"],
        "drum_resource": "A",
        "projects": [{
            "name": "Test",
            "deadline_day": 50,
            "tasks": [
                {"name": "Task1", "resource": "A", "safe_estimate_days": 5, "depends_on": ["NonExistent"]},
            ]
        }],
    }
    try:
        solve_ccpm(data)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "NonExistent" in str(e)
    print("  ccpm invalid dependency: PASS")


def test_buffer_sim_example():
    """Buffer simulator returns valid results."""
    data = buf_example()
    data["seed"] = 42  # fix seed for reproducibility in test
    result = simulate_buffers(data)

    assert result["simulations"] == 10000
    assert result["target_confidence"] == 0.95

    # Percentiles should be monotonically increasing
    p = result["percentiles"]
    assert p["p50"] <= p["p75"] <= p["p90"] <= p["p95"] <= p["p99"]

    # Buffer should be positive
    for method, value in result["buffer_methods"].items():
        assert value > 0, f"{method} buffer should be positive"

    # Recommendation should exist
    assert result["recommendation"]["buffer_size"] > 0

    print("  buffer_sim: PASS")


def test_buffer_sim_degenerate():
    """Buffer simulator handles degenerate distributions (opt==ml==pess)."""
    data = {
        "tasks": [
            {"name": "Fixed", "optimistic": 5, "most_likely": 5, "pessimistic": 5},
            {"name": "Normal", "optimistic": 3, "most_likely": 5, "pessimistic": 10},
        ],
        "target_confidence": 0.95,
        "simulations": 1000,
        "seed": 42,
    }
    result = simulate_buffers(data)
    assert result["simulations"] == 1000
    # Should not crash
    print("  buffer_sim degenerate: PASS")


if __name__ == "__main__":
    print("Running TOC solver tests...\n")
    tests = [
        test_product_mix_example,
        test_product_mix_empty,
        test_product_mix_zero_capacity,
        test_dbr_scheduler_example,
        test_dbr_auto_drum,
        test_ccpm_example,
        test_ccpm_dependency_order,
        test_ccpm_invalid_dependency,
        test_buffer_sim_example,
        test_buffer_sim_degenerate,
    ]

    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"  {test.__name__}: FAIL — {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"  {passed} passed, {failed} failed, {passed+failed} total")
    print(f"{'='*40}")
    sys.exit(1 if failed > 0 else 0)
