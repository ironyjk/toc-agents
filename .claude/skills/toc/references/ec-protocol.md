# Evaporating Cloud Protocol

Resolves conflicts by surfacing and breaking hidden assumptions.
Based on Goldratt's "Evaporating Cloud" (also called Conflict Resolution Diagram) from "It's Not Luck" (1994).

## When This Tool Applies

- Two positions/actions appear mutually exclusive
- A dilemma where "both sides are right"
- A tradeoff that feels forced ("we can't have both X and Y")
- A policy conflict ("department A wants X, department B wants Y")
- A personal decision with competing priorities

## Core Structure

An Evaporating Cloud has exactly 5 entities connected by necessity arrows:

```
A (Common Objective)
├── B (Need #1)  ──→  D (Want #1 / Action #1)
│                          ↕ CONFLICT
└── C (Need #2)  ──→  D' (Want #2 / Action #2)
```

- **A**: The shared objective both sides agree on
- **B**: A necessary condition for A (first perspective)
- **C**: A necessary condition for A (second perspective)
- **D**: What B requires — the action/position of side 1
- **D'**: What C requires — the action/position of side 2
- **D and D' are in direct conflict** — they cannot both be true simultaneously

Every arrow is a NECESSITY relationship: "In order to have [start], we MUST have [end]."

---

## Phase 1: Construct the Cloud

### Step 1.1 — Identify the Conflict (D vs D')

Start from the user's problem. Find two positions, actions, or decisions that appear mutually exclusive.

**Template**: "On one hand we need to **[D]**. On the other hand we need to **[D']**. We can't do both because **[surface reason]**."

**Validation checks:**
- D and D' must be ACTIONS or POSITIONS, not abstract values
- They must genuinely conflict (doing D makes D' impossible, or vice versa)
- They should NOT be "do it" vs "don't do it" — that's a fake conflict. Find the REAL two competing actions.

**Common mistake**: "Should we expand or not?" → This is not a real conflict. The real conflict might be: "Invest in new equipment (D) vs. Build cash reserves (D')"

### Step 1.2 — Identify the Needs (B and C)

For D, ask: **"WHY do we need [D]? What need does it serve?"**
For D', ask: **"WHY do we need [D']? What need does it serve?"**

**Validation**: B and C must be NECESSARY conditions, not just "nice to have."
**Test**: "In order to achieve A, we MUST have B" — if this feels weak, B is not a true need.

**Dig deeper**: If the first answer is shallow ("to save money"), ask again: "Why is saving money necessary HERE? What happens if we don't?"

### Step 1.3 — Identify the Common Objective (A)

Ask: **"What is the shared goal that both B and C serve?"**

**Validation**:
- Both sides must agree A is desirable
- A must be specific enough that B and C feel genuinely necessary
- If A is too vague ("be successful"), narrow it: "Maintain profitability while growing market share"

### Step 1.4 — Validate All Five Arrows

Read each necessity relationship aloud:

| Arrow | Statement | Must feel TRUE |
|-------|-----------|---------------|
| A → B | "In order to [A], we must [B]" | Yes |
| B → D | "In order to [B], we must [D]" | Yes |
| A → C | "In order to [A], we must [C]" | Yes |
| C → D' | "In order to [C], we must [D']" | Yes |
| D ↔ D' | "[D] and [D'] cannot coexist" | Yes |

If any arrow sounds wrong, revise the entity. The cloud must feel logically tight before moving to Phase 2.

---

## Phase 2: Surface Hidden Assumptions

**THIS IS THE CRITICAL STEP.** The cloud "evaporates" when an assumption behind one arrow is shown to be false or breakable.

### Process

For EACH of the 5 arrows (A→B, B→D, A→C, C→D', D↔D'):

Ask: **"WHY do I believe [start] requires [end]? What am I assuming?"**

Generate **at least 3 assumptions per arrow** (5+ for deep mode).

### Format

```
Arrow B→D: "In order to [B: protect cash flow], we must [D: cut costs]"
  Assumption 1: Revenue cannot be increased in the short term
  Assumption 2: All cost categories are equally important
  Assumption 3: Cost-cutting won't damage revenue-generating capacity
  Assumption 4: There are no other ways to protect cash flow
  Assumption 5: The cash flow problem is structural, not timing-related
```

### Assumption Quality Checks

Each assumption must be:
- [ ] A **BELIEF**, not a fact (facts can't be broken)
- [ ] **Specific** enough to challenge ("What if this is NOT true?")
- [ ] **Relevant** to this specific arrow (not a general observation)
- [ ] **Non-trivial** (not just restating the arrow in different words)

### Where to Focus

The richest assumptions are often found in:
1. **A→B and A→C arrows** — people rarely question why their needs are necessary
2. **The conflict arrow (D↔D')** — "Are D and D' REALLY mutually exclusive?"
3. **B→D and C→D' arrows** — "Is this the ONLY action that satisfies this need?"

---

## Phase 3: Break Assumptions → Find Injection

### Process

For each assumption, test: **"Is this assumption ALWAYS true? Under what conditions is it false?"**

When you find a breakable assumption:

1. **State which arrow it breaks** (e.g., "breaks B→D")
2. **State the injection** — the new idea that makes the assumption false
3. **Verify**: With the injection in place, does the conflict dissolve?

### Format

```
BROKEN ASSUMPTION (arrow B→D, assumption #1):
  "Revenue cannot be increased in the short term"

INJECTION:
  "Raise prices on emergency callouts by 15% — win rate data shows 
   price sensitivity is low for urgent work"

VERIFICATION:
  If revenue increases → we don't need cost cuts (D) to protect cash flow (B)
  → The conflict between D and D' dissolves
  → The cloud evaporates ✓
```

### Multiple Injections

Often 2-3 assumptions can be broken. List ALL viable injections.

**Rank each injection by:**

| Criterion | Question |
|-----------|----------|
| Feasibility | Can we actually do this? What's the effort? |
| Impact | Does it fully resolve the conflict, or only partially? |
| Speed | How quickly can we implement it? |
| Risk | What could go wrong? |
| Reversibility | Can we undo it if it doesn't work? |

### Combining Injections

Sometimes no single injection fully resolves the conflict. In that case:
- Identify 2-3 partial injections that together dissolve the cloud
- Explain how they complement each other
- Flag this as a "composite injection"

---

## Phase 4: Output

### Diagram

Render the Evaporating Cloud in the requested format (mermaid or ascii).
Follow the specifications in `output-format.md`.

### Summary

After the diagram, provide:

```
═══ EVAPORATING CLOUD SUMMARY ═══

CONFLICT: [D] vs [D']
OBJECTIVE: [A]

ASSUMPTIONS SURFACED: [total count]
  A→B: [count] assumptions
  B→D: [count] assumptions
  A→C: [count] assumptions
  C→D': [count] assumptions
  D↔D': [count] assumptions

BROKEN ASSUMPTIONS: [count]
  1. [which arrow] — [assumption text]
  2. ...

RECOMMENDED INJECTION:
  [injection text]

INJECTION ASSESSMENT:
  Feasibility: [High/Medium/Low]
  Impact: [Full/Partial]
  Risk: [description]

NEXT STEP: Validate this injection with /toc:frt
```

---

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Fix |
|-------------|---------------|-----|
| D vs D' is "do it" vs "don't do it" | Fake conflict — no real alternative | Find the REAL competing action |
| A is too vague ("be successful") | B and C won't feel necessary | Narrow A to a specific, measurable goal |
| Assumptions are actually facts | Can't break laws of physics | Only list beliefs that COULD be false |
| Only checking B→D and C→D' | Missing the richest assumptions | Always check all 5 arrows, especially A→B and A→C |
| Injection is "compromise" | Compromise means BOTH sides lose | A true injection means NEITHER side loses |
| Jumping to injection without assumptions | Missing the rigor — just brainstorming | Surface assumptions FIRST, then break them systematically |

---

## Domain-Specific Guidance

### Business Strategy
- Needs (B, C) often involve stakeholders: shareholders want X, customers want Y
- Assumptions often hide in market beliefs: "our customers won't pay more"
- Injections often involve reframing the market or finding new segments

### Software Engineering
- Common conflicts: speed vs quality, features vs stability, build vs buy
- Assumptions often hide in technical beliefs: "we can't do X without Y"
- Injections often involve architectural changes or tooling

### Operations/Manufacturing
- Common conflicts: throughput vs quality, utilization vs flexibility
- Assumptions often hide in process beliefs: "we must batch to be efficient"
- Injections often involve TOC's own principles (small batches, pull systems)

### Personal/Team
- Common conflicts: work vs life, growth vs safety, autonomy vs alignment
- Assumptions often hide in identity beliefs: "if I do X, people will think Y"
- Injections often involve redefining success criteria

---

## Handoff

When used in the full TOC workflow (`/toc`):
- **Receives from CRT**: Root cause conflicts (core conflict statement)
- **Passes to FRT**: Injection(s) as proposed changes to validate

Output format for FRT handoff:
```
INJECTION FOR FRT VALIDATION:
  Injection: [text]
  Broken assumption: [text]
  Expected primary effect: [text]
  Concern areas: [list of areas where NBRs might appear]
```
