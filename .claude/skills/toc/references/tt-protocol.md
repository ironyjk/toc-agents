# Transition Tree Protocol

Creates a detailed step-by-step execution plan where each step shows:
the current reality, the action to take, and the expected effect.
Each step's effect becomes the next step's reality.

Based on Goldratt's combined sufficiency + necessity logic from "It's Not Luck" (1994).

## When This Tool Applies

- You have a clear objective but need detailed "how" steps
- You want to communicate an implementation plan that others can follow
- You need to verify that each step logically leads to the next
- You've identified intermediate objectives (via PRT) and need action plans for each

## Core Concept

A TT answers: **"How to cause the change?"** (specifically: what steps, in what order?)

Each node in a TT is a triplet:

```
[Current Reality] + [Action] → [Expected Effect]
```

The Expected Effect of step N becomes the Current Reality of step N+1.

This creates an unbroken chain from "where we are now" to "where we want to be."

---

## Phase 1: List Objectives

If receiving from PRT, use the sequenced IOs.
If standalone, break the user's goal into 2-5 intermediate objectives.

For each objective:
- State it clearly and measurably
- Note any prerequisites (which other objectives must be done first?)

---

## Phase 2: Build Transition Chains

For each objective, build a chain of steps:

### Step Template

```
STEP [N]:
  REALITY: [what is currently true at this point]
  NEED: [why we need to act — connects to the objective]
  ACTION: [specific action to take]
  EFFECT: [what will be true after the action]
```

### Building the Chain

1. **Start**: Current Reality = the actual current state
2. **Ask**: "What is the FIRST action we can take right now?"
3. **Project**: "If we take that action, given the current reality, what effect will it have?"
4. **Loop**: The effect becomes the new reality. Ask: "Now what?"
5. **End**: When the effect matches (or enables) the objective

### Logic Validation

Each step uses BOTH types of logic:

**Necessity** (why):
> "In order to [objective], we must [action], because [reality requires it]"

**Sufficiency** (what happens):
> "If [reality] AND [action], then [effect]"

### Granularity Guidelines

| Depth | Steps per Objective |
|-------|-------------------|
| Shallow | 3-5 steps |
| Deep | 6-10 steps |

**Too granular**: "Open laptop, launch browser, navigate to URL" — combine into meaningful actions
**Too coarse**: "Redesign the system" — break into specific, doable actions

**Rule of thumb**: Each action should be completable by one person in one sitting (minutes to hours, not days).

---

## Phase 3: Validate Each Step

For each step in the chain:

### Sufficiency Check
> "Given [reality] and [action], is the [effect] GUARANTEED?"
- If not, what else is needed? Add an AND connector or prerequisite.

### Reality Check
> "Is [reality] actually true at this point in the chain?"
- If step 3's reality doesn't match step 2's effect, there's a gap.

### Action Feasibility
> "Can we actually DO [action] given [reality]?"
- If not, we need an earlier step to make it possible.

### Effect Verification
> "How will we KNOW [effect] has occurred?"
- Each effect should be observable/measurable.

### Risk Points

Flag steps where:
- The effect is uncertain (mark with "VERIFY:")
- External dependencies exist (mark with "DEPENDS:")
- Failure would be costly to reverse (mark with "CHECKPOINT:")

---

## Phase 4: Output

### Diagram

Render the TT in the requested format (mermaid or ascii).
Follow the specifications in `output-format.md`.

For TT, use `graph LR` (left-to-right, showing sequential flow).

### Summary

```
═══ TRANSITION TREE SUMMARY ═══

OBJECTIVE: [text]

STEPS: [count]

Step 1:
  Reality: [current state]
  Action:  [what to do]
  Effect:  [expected result]
  Verify:  [how to confirm]

Step 2:
  Reality: [= Step 1's effect]
  Action:  [what to do next]
  Effect:  [expected result]
  Verify:  [how to confirm]

...

Step N:
  Reality: [= Step N-1's effect]
  Action:  [final action]
  Effect:  [= OBJECTIVE ACHIEVED]
  Verify:  [how to confirm]

RISK CHECKPOINTS:
  - After Step [N]: [what to verify before continuing]

ESTIMATED EFFORT:
  - Steps 1-2: [quick wins, can start immediately]
  - Steps 3-4: [medium effort]
  - Steps 5+: [larger effort, may need resources]

DEPENDENCIES:
  - Step [N] requires [external thing]
  - Step [N] depends on [other objective] being complete
```

---

## Multiple Objectives

When building TTs for multiple objectives from a PRT:

1. Build each objective's TT independently
2. Note cross-dependencies (Step 3 of Objective A must complete before Step 1 of Objective B)
3. Identify parallel tracks (objectives that can be executed simultaneously)
4. Present as a combined execution timeline

```
═══ COMBINED EXECUTION PLAN ═══

TRACK A (Objective 1): Steps A1 → A2 → A3
TRACK B (Objective 2): Steps B1 → B2 → B3
TRACK C (Objective 3): Steps C1 → C2

  Week 1: A1 + B1 (parallel)
  Week 2: A2 + B2 + C1 (parallel, C1 starts after B1)
  Week 3: A3 + B3 + C2
  
SYNC POINTS:
  - After Week 1: Verify A1 and B1 effects before proceeding
  - After Week 2: Gate check — are we on track?
```

---

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Fix |
|-------------|---------------|-----|
| Steps are too vague | "Improve the process" is not actionable | Each action must be specific enough to DO |
| Reality gaps | Step 3's reality doesn't match step 2's effect | Ensure each effect → next reality chain is unbroken |
| Missing verification | No way to know if a step worked | Add observable verification for each effect |
| Everything is sequential | Artificial dependencies waste time | Test: "Can step N start before step N-1 finishes?" |
| No risk checkpoints | Blindly marching forward | Add checkpoints after high-risk or high-cost steps |
| Actions require resources we don't have | Plan is unrealistic | Add prerequisite steps to acquire resources |

---

## Handoff

When used in the full TOC workflow (`/toc`):
- **Receives from PRT**: Sequenced intermediate objectives with dependencies
- **This is the final tool** — output is the executable action plan

The TT output is the deliverable that the user takes and EXECUTES.
