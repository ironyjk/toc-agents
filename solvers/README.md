# TOC Solvers — OR-Tools Mathematical Optimization

Computational solvers that complement the qualitative Thinking Process skills.

## Setup

```bash
pip install ortools numpy
```

## Solvers

### 1. Product Mix Optimizer (`product_mix.py`)

Maximizes total throughput (T) subject to constraint capacity using Linear Programming.

```bash
python solvers/product_mix.py --example
python solvers/product_mix.py --data my_products.json
```

**When to use**: Multiple products competing for limited constraint time. Classic TOC question: "Which products should we prioritize?"

### 2. DBR Scheduler (`dbr_scheduler.py`)

Schedules jobs through multi-stage process using CP-SAT Constraint Programming.

```bash
python solvers/dbr_scheduler.py --example
python solvers/dbr_scheduler.py --data my_jobs.json
```

**When to use**: Sequencing jobs to minimize tardiness while respecting the drum (constraint).

### 3. CCPM Resource Leveler (`ccpm_leveler.py`)

Schedules multiple projects sharing resources, applying CCPM principles.

```bash
python solvers/ccpm_leveler.py --example
python solvers/ccpm_leveler.py --data my_projects.json
```

**When to use**: Multiple projects competing for the same drum resource. Eliminates multitasking.

### 4. Buffer Sizing Simulator (`buffer_sim.py`)

Monte Carlo simulation to determine optimal buffer sizes.

```bash
python solvers/buffer_sim.py --example
python solvers/buffer_sim.py --data my_tasks.json
```

**When to use**: Sizing constraint buffers (DBR) or project buffers (CCPM). Compares three methods: Goldratt's cut-and-paste, Root Sum of Squares, and Monte Carlo.

## Integration with Claude Code Skills

The skills (`/toc:throughput`, `/toc:dbr`, `/toc:ccpm`) can invoke these solvers when the `--solve` flag is used. Claude Code will:

1. Analyze the user's problem qualitatively (Thinking Process)
2. Structure the data as JSON
3. Run the appropriate solver
4. Interpret the results

Example:
```
/toc:throughput "We have 3 products competing for our CNC machine. 
Product A: $500 price, $200 TVC, 30 min on CNC
Product B: $300 price, $100 TVC, 10 min on CNC  
Product C: $800 price, $400 TVC, 60 min on CNC
CNC available 8 hours/day. Max demand: A=20, B=50, C=10" --solve
```

## JSON Input Formats

See each solver's docstring for detailed input format specifications.
All solvers support `--json` flag for machine-readable output.
