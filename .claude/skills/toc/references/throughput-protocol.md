# Throughput Accounting Protocol

A decision-making framework that replaces traditional cost accounting
with three simple measures: Throughput (T), Investment (I), and Operating Expense (OE).

From Goldratt's "The Goal" (1984) and "The Haystack Syndrome" (1990).

## When This Tool Applies

- Evaluating whether to accept a new order/project
- Deciding between make vs. buy
- Evaluating capital investments
- Pricing decisions
- Product mix decisions when capacity is constrained
- Any decision where traditional cost accounting might mislead

## Core Problem with Cost Accounting

Traditional cost accounting allocates overhead to products based on labor hours or machine hours.
This creates "product costs" that don't reflect reality:

- A product may appear "unprofitable" because of overhead allocation, but actually generates
  positive throughput and doesn't consume the constraint
- Decisions based on "product cost" can lead to rejecting profitable work
  and accepting unprofitable work

## The Three Measures

### T — Throughput

**Revenue minus Truly Variable Costs (TVC)**

TVC = costs that change with EACH unit produced:
- Raw materials
- Sales commissions (per-unit)
- Outsourced processing (per-unit)
- Energy directly consumed per unit

TVC does NOT include:
- Labor (people get paid regardless)
- Rent, utilities, depreciation
- Management overhead

```
T = Revenue - TVC (per unit)
Total T = T per unit × units sold
```

### I — Investment (Inventory)

**Money tied up in the system**

- Raw materials in stock
- Work in progress
- Finished goods inventory
- Equipment and buildings
- Any money the system has invested to generate throughput

### OE — Operating Expense

**Money spent to turn Investment into Throughput**

- All labor costs (salaries, benefits)
- Rent, utilities, depreciation
- Management, administration
- All costs that occur regardless of how many units are produced

---

## Decision Framework

### The TOC Decision Rules

For any decision, ask:

| Question | Measure | Goal |
|----------|---------|------|
| How does this affect money COMING IN? | **T** (Throughput) | Maximize |
| How does this affect money STUCK? | **I** (Investment) | Minimize |
| How does this affect money GOING OUT? | **OE** (Operating Expense) | Minimize |

### Priority Order

1. **First**: Maximize T (throughput) — making money
2. **Second**: Minimize I (investment) — money stuck
3. **Third**: Minimize OE (operating expense) — money going out

> Traditional accounting prioritizes OE reduction (cost-cutting).
> TOC prioritizes T increase (making more money).

### Key Metrics

```
Net Profit (NP) = T - OE
Return on Investment (ROI) = NP / I = (T - OE) / I
Productivity = T / OE
Investment Turns = T / I
```

---

## Decision Types

### Accept or Reject an Order

```
IF the order generates positive T (Revenue > TVC):
  AND the order does NOT consume additional constraint time:
    → ACCEPT (pure profit, no constraint impact)
  
  AND the order DOES consume constraint time:
    → Calculate T per constraint unit (T/CU)
    → Compare with other orders competing for constraint time
    → Accept if T/CU is higher than alternatives
    → Otherwise, negotiate price or timeline
  
IF the order generates negative T (Revenue < TVC):
  → REJECT (unless strategic value justifies the loss)
```

### Product Mix (Which Products to Prioritize)

When the constraint is capacity-limited:

1. Calculate T per unit for each product
2. Calculate constraint time per unit for each product
3. Calculate **T per constraint unit (T/CU)** = T / constraint time
4. Rank products by T/CU (highest first)
5. Fill constraint capacity with highest T/CU products first

```
PRODUCT MIX ANALYSIS:

Product | Price | TVC | T/unit | Constraint min | T/CU
--------|-------|-----|--------|---------------|------
   A    | $100  | $30 |  $70   |     15 min    | $4.67/min
   B    | $80   | $20 |  $60   |     10 min    | $6.00/min ← PRIORITIZE
   C    | $150  | $80 |  $70   |     30 min    | $2.33/min

Priority: B first, then A, then C (if constraint time remains)
```

### Make vs. Buy

```
IF buying frees constraint time:
  Value of freed time = T/CU × freed minutes
  Cost of buying = purchase price - TVC saved
  
  IF value of freed time > cost of buying:
    → BUY (even if "unit cost" appears higher)
  
IF buying doesn't affect the constraint:
  Compare purchase price with TVC only (not "full cost")
```

### Capital Investment

```
Delta-T = Change in throughput
Delta-I = Change in investment
Delta-OE = Change in operating expense

Payback = Delta-I / (Delta-T - Delta-OE)
ROI = (Delta-T - Delta-OE) / Delta-I

Accept if ROI > hurdle rate AND payback < acceptable period
```

---

## Analysis Template

For each option being evaluated:

```
═══ THROUGHPUT ACCOUNTING ANALYSIS ═══

DECISION: [what we're deciding]

OPTION A: [description]
  Revenue impact: [+/- amount per period]
  TVC impact: [+/- amount per period]
  T impact (Delta-T): [+/- amount per period]
  I impact (Delta-I): [+/- amount]
  OE impact (Delta-OE): [+/- amount per period]
  Constraint impact: [consumes/frees X minutes per period]
  
  NP impact: Delta-T - Delta-OE = [amount per period]
  ROI: NP / Delta-I = [%]

OPTION B: [description]
  [same analysis]

COMPARISON:
  ┌─────────┬──────────┬──────────┬──────────┐
  │ Measure │ Option A │ Option B │ Better   │
  ├─────────┼──────────┼──────────┼──────────┤
  │ T       │ [value]  │ [value]  │ [A or B] │
  │ I       │ [value]  │ [value]  │ [A or B] │
  │ OE      │ [value]  │ [value]  │ [A or B] │
  │ NP      │ [value]  │ [value]  │ [A or B] │
  │ ROI     │ [value]  │ [value]  │ [A or B] │
  └─────────┴──────────┴──────────┴──────────┘

CONSTRAINT ANALYSIS:
  Current constraint: [name]
  Option A impact on constraint: [description]
  Option B impact on constraint: [description]

RECOMMENDATION: [Option A / Option B]
RATIONALE: [why, referencing T/I/OE and constraint impact]
```

---

## Common Traps

| Trap | Traditional Thinking | TOC Thinking |
|------|---------------------|-------------|
| "This product loses money" | Unit cost > price (allocated overhead) | T > 0 and doesn't consume constraint → KEEP IT |
| "We should outsource to save costs" | Labor cost is too high | Outsourcing frees constraint time? Calculate T/CU value |
| "Cut the lowest margin product" | Gross margin is low | T/CU might be highest — cutting it REDUCES profit |
| "Maximize machine utilization" | High utilization = efficiency | Only constraint utilization matters; non-constraint idle time is GOOD |
| "Overtime is expensive" | OE goes up | If overtime is at the constraint, Delta-T >>> Delta-OE |

---

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Fix |
|-------------|---------------|-----|
| Using allocated costs for decisions | Allocation distorts product profitability | Use T (revenue - TVC) only |
| Optimizing OE first | Cost-cutting hits T-generating capacity | Optimize T first, then OE |
| Ignoring constraint impact | A decision may be T-positive but constraint-negative | Always check: does this consume constraint time? |
| Comparing options by unit cost | Misleading when overhead is large | Compare by T, T/CU, and constraint impact |
| Treating all resources equally | Only the constraint matters for throughput | Weight decisions by constraint impact |
