# Future Reality Tree Protocol

Validates proposed solutions by projecting their effects forward in time,
identifying both positive outcomes (Desirable Effects) and negative side-effects
(Negative Branch Reservations), then trimming the negatives.

Based on Goldratt's sufficiency logic from "It's Not Luck" (1994).

## When This Tool Applies

- You have a proposed solution and want to check if it will ACTUALLY work
- You want to anticipate unintended consequences BEFORE implementing
- You need to convince stakeholders the solution is sound
- You've resolved a conflict (via EC) and need to validate the injection
- You want to stress-test an idea before committing resources

## Core Concept

A FRT answers: **"Will this solution work? What could go wrong?"**

It's the opposite of a CRT:
- CRT traces backward from symptoms to root causes (What IS causing problems?)
- FRT traces forward from an injection to projected effects (What WILL happen if we do this?)

---

## Phase 1: State the Injection and Primary Effects

### Define the Injection

The injection is a change that doesn't currently exist in the system. State it clearly:

```
INJECTION: [specific action or change]
CONTEXT: [what problem this addresses]
EXPECTED OUTCOME: [what we hope will happen]
```

### Trace Primary Effects (1st order)

Ask: **"If we [injection], what is the IMMEDIATE, DIRECT effect?"**

List 2-4 primary effects. Each must follow sufficiency logic:
- "If [injection], then [primary effect]"
- The injection ALONE must be sufficient to cause the effect
- If not sufficient alone, identify what ELSE is needed (AND connector)

### Validation

For each primary effect:
- Is this a REALISTIC outcome, not wishful thinking?
- Would skeptics agree this effect is likely?
- Is there evidence from similar situations?

---

## Phase 2: Trace Higher-Order Effects

### Secondary Effects (2nd order)

For each primary effect, ask: **"If [primary effect], then what?"**

### Tertiary Effects (3rd order)

Continue tracing: **"If [secondary effect], then what?"**

### Desirable Effects (DEs)

Mark positive outcomes as DEs. These should map back to the original UDEs from the CRT:

```
Original UDE: "Projects miss deadlines"
Corresponding DE: "Projects complete on or before deadline"
```

**Success criterion**: The FRT should show that the injection produces DEs that are the OPPOSITE of the original UDEs. If it doesn't, the injection is insufficient.

### Depth Guidelines

| Depth | Levels | Typical Node Count |
|-------|--------|--------------------|
| Shallow | 2-3 levels | 8-12 nodes |
| Deep | 4-5 levels | 15-25 nodes |

### AND Connectors

When an effect requires the injection PLUS an existing condition:

```
[Injection] ──┐
               ├── AND ──→ [Effect]
[Existing condition] ──┘
```

This is common — most injections work in combination with existing reality, not in isolation.

---

## Phase 3: Identify Negative Branch Reservations (NBRs)

**THIS IS THE CRITICAL STEP.** Every solution has side-effects. Finding them now is cheaper than finding them after implementation.

### What is an NBR?

A Negative Branch Reservation is an undesirable effect that the injection ALSO causes, alongside the positive effects. It's a legitimate concern that the injection might make some things WORSE.

### How to Find NBRs

For each entity in the tree (injection, primary effects, secondary effects):

Ask these questions:
1. **"What ELSE could [this entity] cause?"** — Look for branching paths
2. **"Who might be negatively affected?"** — Think about all stakeholders
3. **"What could go wrong?"** — Murphy's Law analysis
4. **"What assumptions are we making about the environment?"** — Context might change
5. **"Has this been tried before? What happened?"** — Historical precedent

### NBR Quality Criteria

An NBR must be:
- [ ] A genuine NEGATIVE effect (not just an inconvenience)
- [ ] CAUSED by the injection or its effects (traceable chain)
- [ ] REALISTIC (not paranoid worst-case fantasy)
- [ ] SPECIFIC (not vague "things could go wrong")

### Common NBR Categories

| Category | Example |
|----------|---------|
| Resource diversion | "Training costs reduce Q1 budget" |
| Resistance/morale | "Senior staff feel undermined by delegation" |
| Quality/safety risk | "Faster decisions mean less thorough review" |
| Dependency creation | "New process requires tool that might not scale" |
| Timing conflict | "Implementation disrupts peak season operations" |
| Unintended incentive | "Metric gaming: people optimize the measure, not the outcome" |

---

## Phase 4: Trim NBRs

### What is Trimming?

Trimming means adding conditions, safeguards, or modifications to the injection that prevent the NBR from occurring — WITHOUT weakening the positive effects.

### Process

For each NBR:

1. **Identify the branch point** — where does the negative effect split from the positive chain?
2. **Design a trim** — what additional action prevents the NBR?
3. **Verify the trim works** — does it actually block the NBR?
4. **Verify no damage** — does the trim weaken any positive effects?

### Format

```
NBR: "Junior staff makes poor approval decisions"
  Branch point: Injection → "Junior staff now has approval authority"
  TRIM: "Implement tiered approval limits: <$5K junior, <$25K manager, >$25K director"
  Verification: Trim limits exposure while maintaining speed benefit for 80% of decisions
  Side-effects of trim: None identified
```

### Trim Quality Checks

- [ ] The trim addresses the ROOT of the NBR, not just the symptom
- [ ] The trim doesn't create its own new NBRs (if it does, trim THOSE too)
- [ ] The trim is practical and implementable
- [ ] The trim doesn't significantly weaken the positive effects
- [ ] The trim doesn't require more effort than the original injection

### Untrimable NBRs

If an NBR cannot be trimmed:
- State this clearly: "This NBR cannot be adequately trimmed"
- Assess its severity relative to the benefits
- This may mean the injection needs to be redesigned (go back to EC)

---

## Phase 5: Output

### Diagram

Render the FRT in the requested format (mermaid or ascii).
Follow the specifications in `output-format.md`.

Key elements:
- Injection at the bottom (green)
- DEs flowing upward (teal)
- NBRs branching off to the side (yellow)
- Trims connected to NBRs (purple)
- Dotted arrows for NBR connections

### Summary

```
═══ FUTURE REALITY TREE SUMMARY ═══

INJECTION: [text]

DESIRABLE EFFECTS: [count]
  1. [DE text] — resolves UDE: [original UDE if known]
  2. [DE text]
  ...

NEGATIVE BRANCH RESERVATIONS: [count]
  1. [NBR text]
     TRIM: [trim text]
     Status: Trimmed ✓
  2. [NBR text]
     TRIM: [trim text]
     Status: Trimmed ✓
  3. [NBR text]
     Status: UNTRIMMED ✗ — [reason]

OVERALL ASSESSMENT:
  [PROCEED / PROCEED WITH CONDITIONS / RECONSIDER]

  Positive effects: [count] DEs achieved
  Risks managed: [count] NBRs trimmed
  Residual risks: [count] untrimmed NBRs
  
  [Brief qualitative assessment: Does the injection solve the original problem?
   Are the trimmed NBRs manageable? Is the net effect positive?]

NEXT STEP: Plan implementation with /toc:prt
```

---

## Assessment Framework

### PROCEED
- All or most UDEs are addressed by DEs
- All NBRs are trimmed or negligible
- Net effect is clearly positive

### PROCEED WITH CONDITIONS
- Most UDEs are addressed
- Some NBRs require monitoring or additional trims
- Net effect is positive but requires vigilance

### RECONSIDER
- Key UDEs are NOT addressed
- Critical NBRs cannot be trimmed
- Net effect is unclear or negative
- Recommendation: return to EC and find a different injection

---

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Fix |
|-------------|---------------|-----|
| No NBRs found | Every injection has side-effects | Try harder — use all 5 NBR questions |
| NBRs are vague fears | "Something might go wrong" is not useful | Make each NBR specific and traceable |
| Trims are bigger than the injection | The cure is worse than the disease | Simplify — or find a different injection |
| Only positive effects | This is cheerleading, not analysis | Actively look for negative branches |
| Ignoring stakeholder perspective | Different people experience effects differently | Check effects on ALL affected parties |

---

## Handoff

When used in the full TOC workflow (`/toc`):
- **Receives from EC**: Injection(s) and broken assumptions
- **Passes to PRT**: Validated solution with trims

Output format for PRT handoff:
```
FRT RESULTS FOR PRT:
  Validated injection: [text]
  Required trims: [list]
  Implementation goal: [the DEs we need to achieve]
  Known risks to monitor: [untrimmed or partially trimmed NBRs]
  Success criteria: [how we'll know it worked]
```
