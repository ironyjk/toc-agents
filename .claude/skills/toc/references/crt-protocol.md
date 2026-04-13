# Current Reality Tree Protocol

Maps cause-effect chains from observable Undesirable Effects (UDEs) down to 1-3 root causes.
Based on Goldratt's sufficiency logic ("If...Then...") from "It's Not Luck" (1994).

## When This Tool Applies

- Multiple symptoms with no clear connection
- Recurring problems that resist individual fixes
- "Whack-a-mole" situations — fixing one thing breaks another
- Need to find the ONE thing to change that fixes MANY problems
- Feeling overwhelmed by too many issues

## Core Concept

A CRT answers: **"What to change?"**

It works by:
1. Listing observable symptoms (UDEs)
2. Connecting them via cause-effect logic (If...Then...)
3. Tracing chains downward until reaching root causes
4. Identifying the 1-3 root causes that explain ALL the UDEs

The power of a CRT is the **V-shape**: one root cause at the bottom fans out to explain multiple UDEs at the top. The deeper and wider the V, the higher the leverage.

---

## Phase 1: Gather UDEs

### From a Problem Description

If the user provides a narrative, extract UDEs by looking for:
- Complaints ("We keep missing deadlines")
- Negative trends ("Quality has declined")
- Frustrations ("Employees are leaving")
- Failures ("The launch failed")
- Gaps ("Revenue is below target")

### From a Vague Complaint

If the problem is vague ("things aren't working"), use AskUserQuestion:

```
header: "Symptoms"
question: "List 3-5 specific things that are going wrong. Be concrete: who is affected, what's happening, how bad is it?"
```

### UDE Quality Criteria

Each UDE must be:

| Criterion | Test | Bad Example | Good Example |
|-----------|------|-------------|-------------|
| Observable | Can someone point to evidence? | "Culture is bad" | "3 senior engineers resigned in Q1" |
| Undesirable | Stakeholder agrees it's a problem? | "We use microservices" | "Deployment takes 4 hours" |
| Complete sentence | Not a fragment or keyword? | "Quality" | "Product defect rate increased from 2% to 8%" |
| Not a cause | Is it a SYMPTOM, not an explanation? | "Poor training" | "New hires take 6 months to reach productivity" |
| Not a solution | Is it a PROBLEM, not a fix? | "We need more devs" | "Feature backlog has grown to 200 items" |

### Target UDE Count

| Depth | UDE Count | Root Causes |
|-------|-----------|-------------|
| Shallow | 5-8 | 1-2 |
| Deep | 10-15 | 2-4 |

---

## Phase 2: Connect UDEs via Cause-Effect

### Bottom-Up Construction

Start with any UDE. Ask: **"WHY does [UDE] exist? What CAUSES it?"**

For each cause found:
1. Is this cause itself a UDE from our list? → **Connect them** (arrow from cause-UDE to effect-UDE)
2. Is this a new observable fact? → **Add as intermediate entity**
3. Keep asking "why" until you reach entities that are:
   - **Within our control** (potential root causes)
   - **OR external facts we cannot change** (given reality/constraints)

### Sufficiency Logic

Every arrow means: **"If [cause], then [effect]"**

The cause must be SUFFICIENT — it alone produces the effect. If it needs help:

**AND Connector**: When two causes are BOTH needed:
```
[Cause A] ──┐
             ├── AND ──→ [Effect]
[Cause B] ──┘
```

**Test**: "If [Cause A] alone, would [Effect] still happen?" 
- If YES → single arrow (A is sufficient)
- If NO → AND connector (both A and B needed)

### Categories of Legitimate Reservation (CLR)

For EVERY arrow in the tree, verify:

| # | Check | Question | If fails... |
|---|-------|----------|-------------|
| 1 | Clarity | Is the cause clearly stated? | Rewrite as complete sentence |
| 2 | Entity Existence | Does this cause actually exist? Evidence? | Remove if unverified |
| 3 | Causality | Does the cause ACTUALLY produce the effect? | Remove arrow |
| 4 | Sufficiency | Is the cause ALONE sufficient? | Add AND connector |
| 5 | Additional Cause | Are there OTHER independent causes? | Add parallel arrows |
| 6 | Cause-Effect Reversal | Is the arrow backwards? | Reverse it |
| 7 | Predicted Effect | What OTHER effects should this cause produce? Do they exist? | If not, question the cause |
| 8 | Tautology | Is this just restating the effect? | Remove — find real cause |

**You don't need to check all 8 for every arrow.** Focus on:
- #3 (Causality) and #4 (Sufficiency) for every arrow
- #6 (Reversal) when unsure about direction
- #8 (Tautology) when the cause sounds like the effect

### Connection Strategies

When stuck connecting UDEs:

1. **Look for common words** — UDEs mentioning similar topics may be connected
2. **Look for timing** — earlier problems likely cause later ones
3. **Look for departments** — problems often flow across organizational boundaries
4. **Ask "So what?"** — if [cause] happens, then what? Follow the chain UP
5. **Ask "Why?"** — if [effect] exists, why? Follow the chain DOWN

---

## Phase 3: Identify Root Causes

### The V-Shape Test

A root cause:
1. Is at the **BOTTOM** of the tree (nothing causes it within the system)
2. **Causes multiple UDEs** through branching chains upward
3. Is **within our sphere of influence** (we can change it)

The wider the V (more UDEs explained), the higher the leverage.

### Root Cause Ranking

```
Root Cause Score = (UDEs explained) × (average severity of those UDEs)
```

| Score | Leverage |
|-------|----------|
| Explains 1-2 UDEs | Low — probably not a root cause, dig deeper |
| Explains 3-5 UDEs | Medium — likely a real root cause |
| Explains 6+ UDEs | High — this is THE constraint |

### Common Root Cause Patterns

| Pattern | Example | Signal |
|---------|---------|--------|
| Policy constraint | "All decisions require VP approval" | Multiple delays, workarounds, frustration |
| Measurement conflict | "KPI rewards utilization, not throughput" | Busy but unproductive, local optima |
| Missing capability | "No automated testing" | Quality issues, slow delivery, fear of change |
| Information asymmetry | "Sales doesn't know capacity" | Overpromising, firefighting, missed deadlines |
| Batch mentality | "We wait to have 10 requests before processing" | Long lead times, large WIP, uneven flow |

### Too Many Root Causes?

If you find more than 4 root causes:
- The tree is probably too **shallow** — keep asking "why" to find deeper common causes
- Two "root causes" might actually be effects of a single deeper cause
- External constraints (truly outside your control) should be labeled as **given reality**, not root causes

---

## Phase 4: Render Output

### Diagram

Render the CRT in the requested format (mermaid or ascii).
Follow the specifications in `output-format.md`.

- UDEs at the top (they're the visible symptoms)
- Root causes at the bottom (they're hidden)
- Flow is bottom-to-top (cause → effect)
- AND connectors where multiple causes are required

### Summary

```
═══ CURRENT REALITY TREE SUMMARY ═══

UDEs IDENTIFIED: [N]
  1. [UDE text]
  2. [UDE text]
  ...

ROOT CAUSES: [N] (ranked by leverage)
  1. [ROOT] [text] — explains UDEs #[list] ([count] UDEs)
  2. [ROOT] [text] — explains UDEs #[list] ([count] UDEs)

CAUSE-EFFECT HIGHLIGHTS:
  [Root 1] → [key intermediate] → [most impactful UDE]
  [Root 1] → [different path] → [another UDE]

CORE CONFLICT (ready for /toc:ec):
  "[Root cause] persists because of a conflict between
   [what we're doing] and [what we should be doing].
   The underlying dilemma: [D] vs [D']"
```

---

## Phase 5: Identify Core Conflict (for EC Handoff)

The root cause often persists because of an underlying CONFLICT — a policy, behavior, or assumption that exists because of a perceived dilemma.

Ask: **"Why does [root cause] persist? What prevents people from simply eliminating it?"**

Common answers:
- "Because we'd lose [something important]" → That's the other side of the conflict
- "Because [authority figure] believes [something]" → That's a hidden assumption
- "Because we've always done it this way" → That's inertia masking a conflict

### Format for EC Handoff

```
CORE CONFLICT FOR EC:
  Root cause: [text]
  Current behavior (D): [what people are doing that maintains the root cause]
  Alternative behavior (D'): [what they SHOULD be doing but aren't]
  Why the conflict persists: [why people think they can't do D']
  Affected UDEs: #[list]
```

---

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Fix |
|-------------|---------------|-----|
| Solutions as UDEs | "We need more staff" is a solution, not a symptom | Restate as the PROBLEM: "Response time exceeds SLA" |
| Single-chain tree | No branching = missing connections | Look for cross-links between chains |
| Jumping to root cause | Skipping the chain = guessing | Build the full If→Then chain, step by step |
| 10+ root causes | Tree is too shallow | Keep asking "why" to find deeper common causes |
| Circular logic | A→B→A is not valid causality | Break the cycle — find the DEEPER cause |
| All external causes | "Market is bad" is given reality, not a root cause | Focus on what's WITHIN your control |
| No AND connectors | Oversimplifying — most effects have multiple causes | Test sufficiency: "Is this cause ALONE enough?" |

---

## Domain-Specific Guidance

### Business/Organization
- UDEs often cluster around: financial performance, customer satisfaction, employee engagement, operational efficiency
- Root causes often involve: measurement systems, policies, communication structures
- Don't forget: the constraint is rarely "not enough resources" — it's usually a POLICY

### Software/Technology
- UDEs often cluster around: delivery speed, quality/bugs, technical debt, team productivity
- Root causes often involve: architecture decisions, testing practices, deployment processes
- Look for: batch sizes (large PRs, infrequent releases) as hidden root causes

### Manufacturing/Operations
- UDEs often cluster around: throughput, quality, lead time, inventory, overtime
- Root causes often involve: batch policies, local efficiency metrics, scheduling rules
- Classic TOC territory: apply Drum-Buffer-Rope thinking

### Personal/Team
- UDEs often cluster around: overwork, missed goals, relationship strain, health
- Root causes often involve: unclear priorities, inability to say no, perfectionism
- The "constraint" is often TIME — but the real question is what POLICY governs time allocation

---

## Handoff

When used in the full TOC workflow (`/toc`):
- **Passes to EC**: Core conflict (Phase 5 output)
- EC will resolve the conflict and produce an injection
- That injection then goes to FRT for validation

Output format for EC handoff:
```
CRT RESULTS FOR EC:
  Root cause: [text]
  Core conflict: [D] vs [D']
  Underlying dilemma: [description]
  UDEs that would be resolved: [list]
  Severity assessment: [High/Medium/Low]
```
