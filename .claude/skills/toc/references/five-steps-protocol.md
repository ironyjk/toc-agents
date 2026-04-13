# Five Focusing Steps Protocol

The foundation of the Theory of Constraints — a continuous improvement cycle
for identifying and eliminating the system's bottleneck.

From Goldratt's "The Goal" (1984).

## When This Tool Applies

- System throughput is below expectations
- Resources seem busy but output is low
- Adding capacity doesn't seem to help
- Different parts of the system blame each other
- You want to find the ONE thing to improve that has maximum impact
- You suspect local optimization is hurting global performance

## The Five Steps

```
1. IDENTIFY → 2. EXPLOIT → 3. SUBORDINATE → 4. ELEVATE → 5. REPEAT
     ↑                                                          │
     └──────────────────────────────────────────────────────────┘
```

> "Any improvement NOT at the constraint is an illusion." — Goldratt

---

## Step 1: IDENTIFY the System's Constraint

### What is a Constraint?

The constraint is the resource, policy, or condition that limits the system's throughput.
It is the bottleneck — the weakest link in the chain.

### How to Find It

| Method | How | Signal |
|--------|-----|--------|
| **WIP accumulation** | Look for where work piles up | Inventory/queue before the constraint |
| **Wait time** | Measure how long work waits at each stage | Longest wait = constraint |
| **Utilization** | Measure capacity usage at each stage | Near 100% = likely constraint |
| **Starving downstream** | Check what's idle waiting for input | Idle resources fed by the constraint |
| **Ask people** | "What are you always waiting for?" | Everyone points to the same thing |

### Types of Constraints

| Type | Example | How to spot |
|------|---------|-------------|
| **Physical** | A machine, person, or resource | Visible queue, high utilization |
| **Policy** | A rule, procedure, or measurement | "We can't because the policy says..." |
| **Market** | Demand is less than capacity | System is underutilized but profitable |
| **Paradigm** | A belief or assumption | "That's just how it's done" |

> **Important**: Policy constraints are the most common and most invisible.
> A policy constraint masquerades as "just how things work."

### Output

```
CONSTRAINT IDENTIFIED:
  Type: [physical / policy / market / paradigm]
  Location: [where in the system]
  Evidence: [how we know this is the constraint]
  Impact: [how much it limits throughput]
  Current throughput: [metric] per [time unit]
```

---

## Step 2: EXPLOIT the Constraint

### Principle

Squeeze maximum output from the constraint WITHOUT spending money.
The constraint is too precious to waste on:
- Downtime (breaks, changeovers, setups)
- Defects (processing bad inputs that will be rejected later)
- Non-constraint work (tasks that don't directly contribute to throughput)

### Exploitation Strategies

| Strategy | Question to Ask |
|----------|----------------|
| **Eliminate waste** | "Is the constraint ever idle? Why?" |
| **Quality gate BEFORE** | "Does the constraint process work that later fails?" |
| **Prioritize** | "Is the constraint working on the most important things first?" |
| **Offload** | "Is the constraint doing anything a non-constraint could do?" |
| **Buffer** | "Is there always work READY for the constraint?" |
| **Reduce setup** | "How much time does the constraint spend on changeovers?" |

### Output

```
EXPLOITATION PLAN:
  Current utilization: [X]%
  Wasted capacity:
    - [waste 1]: [amount]
    - [waste 2]: [amount]
  
  Actions (no investment required):
    1. [action] → expected gain: [amount]
    2. [action] → expected gain: [amount]
    3. [action] → expected gain: [amount]
  
  Expected throughput after exploitation: [metric] per [time unit]
  Improvement: [X]% increase
```

---

## Step 3: SUBORDINATE Everything Else

### Principle

Every non-constraint process must serve the constraint's needs.
This means non-constraints will deliberately have EXCESS capacity — and that's correct.

### Common Subordination Actions

| Action | What it means |
|--------|--------------|
| **Match pace** | Non-constraints produce only what the constraint can process |
| **Buffer the constraint** | Maintain a time buffer before the constraint |
| **Don't optimize non-constraints** | High local efficiency at non-constraints is HARMFUL if it overloads the constraint |
| **Adjust schedules** | Align release schedules to constraint capacity |
| **Protect constraint time** | Don't interrupt the constraint for non-critical tasks |

### The Drum-Buffer-Rope Analogy

- **Drum**: The constraint sets the pace (like a drummer in a march)
- **Buffer**: Time buffer protects the constraint from upstream disruptions
- **Rope**: Signals from the constraint control when upstream starts new work

### Signs of Failed Subordination

- WIP is growing everywhere
- Non-constraints are "busy" but the constraint is starved
- Expediting is common ("rush this through!")
- People say "we're all bottlenecks" (no — there's ONE constraint)

### Output

```
SUBORDINATION PLAN:
  Non-constraints affected:
    1. [process/resource] — current behavior: [X], new behavior: [Y]
    2. [process/resource] — current behavior: [X], new behavior: [Y]
  
  Buffers needed:
    - Before constraint: [time/WIP buffer size]
    - After constraint: [shipping buffer if needed]
  
  Policies to change:
    - [old policy] → [new policy]
  
  Metrics to change:
    - STOP measuring: [local efficiency metrics]
    - START measuring: [throughput, constraint utilization, on-time delivery]
```

---

## Step 4: ELEVATE the Constraint

### Principle

Only AFTER fully exploiting and subordinating, invest to increase constraint capacity.
This usually costs money — buy equipment, hire people, add shifts, upgrade systems.

### Why Elevate LAST (Not First)

Most organizations jump straight to "buy more" without exploiting what they have.
Result: expensive investment with marginal improvement because the real waste wasn't addressed.

**Rule**: Exploitation (Step 2) typically yields 20-50% improvement for free.
Only elevate when exploitation gains are exhausted.

### Elevation Strategies

| Strategy | When to use |
|----------|-------------|
| **Add capacity** | Physical constraint: buy machine, hire person |
| **Change policy** | Policy constraint: rewrite the rule |
| **Outsource** | Constraint work can be partially externalized |
| **Redesign** | Architecture change that eliminates the constraint entirely |
| **Automate** | Technology can replace the bottleneck step |

### Output

```
ELEVATION PLAN:
  Investment required: [cost estimate]
  Options:
    1. [option] — cost: [X], capacity gain: [Y]%, timeline: [Z]
    2. [option] — cost: [X], capacity gain: [Y]%, timeline: [Z]
  
  Recommended: [option]
  Expected throughput after elevation: [metric] per [time unit]
  ROI: [estimate]
```

---

## Step 5: REPEAT — Has the Constraint Moved?

### Principle

After elevation, the constraint has likely moved to a different part of the system.
**DO NOT let inertia become the new constraint.**

### Process

1. Re-examine the system: Where does work pile up NOW?
2. The old constraint is no longer the bottleneck
3. The new constraint may be in a completely different place
4. Go back to Step 1 with the new constraint

### The Inertia Warning

> "The biggest danger is that a solution to yesterday's constraint becomes 
> tomorrow's policy constraint." — Goldratt

Example: You added a second machine (elevation). But the scheduling policy still treats 
the original machine as the bottleneck. Now the scheduling policy IS the constraint.

### Output

```
CONSTRAINT SHIFT ANALYSIS:
  Previous constraint: [text]
  Status after elevation: [no longer limiting]
  
  New constraint candidates:
    1. [resource/policy] — evidence: [why this might be the new bottleneck]
    2. [resource/policy] — evidence: [why this might be the new bottleneck]
  
  WARNING — Inertia risks:
    - [policy/practice that was built around the old constraint]
    - [measurement that assumes the old constraint]
  
  Recommendation: Run Step 1 analysis on [most likely new constraint]
```

---

## Full Output Format

```
═══ FIVE FOCUSING STEPS ANALYSIS ═══

SYSTEM: [description]
GOAL: [what throughput means for this system]

━━━ STEP 1: IDENTIFY ━━━
Constraint: [text]
Type: [physical/policy/market/paradigm]
Evidence: [text]
Current throughput: [metric]

━━━ STEP 2: EXPLOIT ━━━
[exploitation actions and expected gains]

━━━ STEP 3: SUBORDINATE ━━━
[subordination changes to non-constraints]

━━━ STEP 4: ELEVATE ━━━
[investment options if exploitation is insufficient]

━━━ STEP 5: REPEAT ━━━
[where the constraint moves next]

━━━ SUMMARY ━━━
Current state: [throughput]
After exploitation: [throughput] (+X%)
After subordination: [throughput] (+Y%)
After elevation: [throughput] (+Z%)
Total potential improvement: [X+Y+Z]%

Priority actions:
1. [immediate — exploit]
2. [short-term — subordinate]
3. [medium-term — elevate]
```

---

## Domain-Specific Guidance

### Manufacturing
- Physical constraints dominate: machines, workstations, operators
- Use Drum-Buffer-Rope scheduling
- Measure: throughput (units/hour), not utilization

### Software Development
- Policy constraints dominate: review processes, deployment gates, meeting load
- Common constraint: a specific person who must approve/review everything
- Measure: lead time (idea to production), not velocity/story points

### Service Business
- Skilled labor is usually the constraint: the expert, the specialist
- Exploit: reduce time experts spend on non-expert tasks
- Subordinate: non-experts prepare everything before the expert touches it

### Sales/Revenue
- Market constraints (not enough demand) require different thinking
- Exploit: improve conversion rates
- Elevate: expand market reach, new channels, new segments

---

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Fix |
|-------------|---------------|-----|
| "Everything is a bottleneck" | There's always ONE primary constraint | Measure: where does WIP accumulate MOST? |
| Elevating before exploiting | Waste of money — free gains come first | Do Steps 2 and 3 BEFORE spending money |
| Optimizing non-constraints | Feels productive but doesn't help throughput | Focus ALL improvement effort on the constraint |
| Ignoring policy constraints | "We've always done it this way" | Ask: "Why does this policy exist? Is the reason still valid?" |
| Measuring local efficiency | Makes people busy, not productive | Measure SYSTEM throughput, not individual busyness |
