# Theory of Constraints — Core Theory Reference

## Origin

Eliyahu M. Goldratt (1947–2011), Israeli physicist turned management thinker.
Core insight: **Every system has at least one constraint that limits its throughput.**

## The Five Focusing Steps

The foundation of TOC — a continuous improvement cycle:

1. **IDENTIFY** the system's constraint (the bottleneck)
2. **EXPLOIT** the constraint (maximize its output with existing resources)
3. **SUBORDINATE** everything else to the constraint (align all processes)
4. **ELEVATE** the constraint (invest to increase its capacity)
5. **REPEAT** — the constraint has moved; go back to step 1

> "Any improvement NOT at the constraint is an illusion." — Goldratt

## The Thinking Processes

Six logical tools for systematic problem-solving. They answer three questions:
- **What to change?** → Current Reality Tree (CRT)
- **What to change to?** → Evaporating Cloud (EC) + Future Reality Tree (FRT)
- **How to cause the change?** → Prerequisite Tree (PRT) + Transition Tree (TT)

### Tool Overview

| Tool | Purpose | Logic Type | Input | Output |
|------|---------|-----------|-------|--------|
| CRT | Find root causes | Sufficiency (If→Then) | Undesirable Effects | Root causes |
| EC | Resolve conflicts | Necessity (Must→To) | Dilemma/conflict | Broken assumption + injection |
| FRT | Validate solutions | Sufficiency (If→Then) | Injections from EC | Validated solution + trimmed NBRs |
| PRT | Plan implementation | Necessity | Goal + obstacles | Intermediate objectives |
| TT | Execute step-by-step | Sufficiency + Necessity | Intermediate objectives | Action sequence |
| 5FS | Find bottleneck | Throughput analysis | System description | Constraint + exploitation plan |

## Sufficiency Logic (If...Then...)

Used in CRT, FRT, and TT. Every arrow means:

```
If [cause] then [effect]
```

The cause is SUFFICIENT to produce the effect. No other conditions needed.

When multiple causes are ALL required:

```
If [cause A] AND [cause B] then [effect]
```

Use an AND connector (ellipse) to show this.

### Validation: Categories of Legitimate Reservation (CLR)

Every cause-effect arrow must survive these 8 challenges:

| # | Reservation | Question |
|---|------------|----------|
| 1 | Clarity | Is the entity clearly stated? Complete sentence? |
| 2 | Entity Existence | Does this actually exist in reality? Evidence? |
| 3 | Causality Existence | Does the cause ACTUALLY produce the effect? |
| 4 | Cause Insufficiency | Is the cause alone sufficient? Or are additional causes needed? |
| 5 | Additional Cause | Are there OTHER causes that could produce this effect? |
| 6 | Cause-Effect Reversal | Is the arrow pointing the right direction? |
| 7 | Predicted Effect Existence | If this cause exists, what OTHER effects should we see? Do they exist? |
| 8 | Tautology | Is this just restating the same thing in different words? |

## Necessity Logic (In order to...we must...)

Used in EC and PRT. Every arrow means:

```
In order to [objective], we must [requirement]
```

The requirement is NECESSARY — without it, the objective cannot be achieved.

### Validation

- "Can we achieve [objective] WITHOUT [requirement]?" — If yes, the arrow is invalid.
- "Is [requirement] the ONLY way to achieve [objective]?" — If no, find alternatives.

## Key Terminology

| Term | Definition |
|------|-----------|
| **UDE** | Undesirable Effect — an observable negative symptom |
| **DE** | Desirable Effect — the positive outcome we want |
| **Injection** | A new idea/action that doesn't currently exist in the system |
| **NBR** | Negative Branch Reservation — an unintended negative side-effect of an injection |
| **Trimming** | Adding conditions to an injection to prevent its NBRs |
| **Root Cause** | The deepest cause in a CRT that drives multiple UDEs |
| **Core Conflict** | The underlying dilemma that sustains the root cause |
| **Constraint** | The factor that limits system throughput |
| **Throughput** | The rate at which the system generates its goal |

## Books Reference

| Book | Year | Focus |
|------|------|-------|
| The Goal | 1984 | TOC fundamentals, Five Focusing Steps |
| It's Not Luck | 1994 | Thinking Processes (EC, CRT, FRT) |
| Critical Chain | 1997 | Project management |
| Necessary But Not Sufficient | 2000 | Technology implementation |
| The Choice | 2008 | Cause-effect thinking, clarity |
| Isn't It Obvious | 2009 | TOC for distribution/retail |
