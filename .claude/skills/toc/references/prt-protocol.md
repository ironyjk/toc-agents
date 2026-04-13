# Prerequisite Tree Protocol

Identifies obstacles between the current state and a goal, then defines
intermediate objectives (IOs) to overcome each obstacle, sequenced by dependency.

Based on Goldratt's necessity logic from "It's Not Luck" (1994).

## When This Tool Applies

- You know WHAT to do but not HOW to get there
- The path to the goal feels blocked by multiple obstacles
- You need to break a large change into achievable steps
- Stakeholders say "we can't do that because..." — each "because" is an obstacle
- You've validated an injection (via FRT) and need an implementation roadmap

## Core Concept

A PRT answers: **"How to cause the change?"** (specifically: what's in the way?)

It works by:
1. Stating the goal (often the injection from EC/FRT)
2. Listing every obstacle preventing the goal
3. For each obstacle, defining an intermediate objective (IO) that overcomes it
4. Sequencing the IOs by dependency (which must come first?)

---

## Phase 1: State the Goal

The goal must be:
- **Specific**: Not "improve things" but "reduce delivery time from 4 weeks to 1 week"
- **Measurable**: How will we know we achieved it?
- **Within scope**: Something the team/organization can actually do

If receiving from FRT, the goal is the validated injection plus its trims.

---

## Phase 2: List Obstacles

### Brainstorming Obstacles

Ask: **"What prevents us from achieving [goal] RIGHT NOW?"**

For each answer, dig deeper:
- "Why is that an obstacle?"
- "Is this a real constraint or a perceived one?"
- "Who or what controls this obstacle?"

### Obstacle Categories

| Category | Examples |
|----------|---------|
| Knowledge gaps | "We don't know how to..." |
| Resource constraints | "We don't have enough..." |
| Policy barriers | "Current rules prohibit..." |
| Technical limitations | "The system can't..." |
| Resistance/politics | "[Person/group] will oppose..." |
| Dependency chains | "We can't do X until Y..." |
| Skill gaps | "Nobody knows how to..." |
| Communication gaps | "[Group] doesn't understand..." |

### Obstacle Quality Criteria

Each obstacle must be:
- [ ] **Real**: Evidence-based, not hypothetical
- [ ] **Specific**: Not "lack of resources" but "need 2 additional engineers with Go experience"
- [ ] **Relevant**: Directly prevents the goal (not a general complaint)
- [ ] **Independent**: Not a consequence of another obstacle (those belong lower in the tree)

### Target Count

| Depth | Obstacles |
|-------|-----------|
| Shallow | 3-5 |
| Deep | 6-10 |

---

## Phase 3: Define Intermediate Objectives (IOs)

For each obstacle, define an IO that OVERCOMES it.

### IO Definition Template

```
OBSTACLE: [what's in the way]
IO: [what we need to achieve to remove this obstacle]
WHY: "In order to [goal], we must [IO], because [obstacle] prevents us"
```

### IO Quality Criteria

Each IO must be:
- [ ] **Achievable**: Can actually be done with available resources
- [ ] **Sufficient**: Actually overcomes the obstacle (not just reduces it)
- [ ] **Verifiable**: We can tell when it's been achieved
- [ ] **Minimal**: Smallest action that overcomes the obstacle (don't over-engineer)

### Necessity Test

For each IO: **"In order to achieve [goal], we MUST achieve [IO]"**
- If this feels wrong, the IO might be optional — remove or downgrade it
- If this feels too weak, the IO might be insufficient — strengthen it

---

## Phase 4: Sequence the IOs

### Dependency Analysis

For each pair of IOs, ask: **"Must [IO-A] be completed before [IO-B] can start?"**

Three relationships:
1. **Sequential**: IO-A must finish before IO-B starts (A → B)
2. **Parallel**: IO-A and IO-B can happen simultaneously
3. **Conditional**: IO-B only needed IF IO-A reveals certain information

### Critical Path

Identify the longest chain of sequential IOs — this is the critical path and determines the minimum time to achieve the goal.

### Quick Wins

Identify IOs that:
- Have no dependencies (can start immediately)
- Are small effort
- Provide visible progress (builds momentum)

Flag these as "START HERE" items.

---

## Phase 5: Output

### Diagram

Render the PRT in the requested format (mermaid or ascii).
Follow the specifications in `output-format.md`.

- Goal at the top
- IOs in the middle (with dependency arrows)
- Obstacles at the bottom (connected to their IOs via dotted arrows)

### Summary

```
═══ PREREQUISITE TREE SUMMARY ═══

GOAL: [text]

OBSTACLES: [count]
  1. [OBS] [text] → IO: [text]
  2. [OBS] [text] → IO: [text]
  ...

IMPLEMENTATION SEQUENCE:
  Phase 1 (parallel — start immediately):
    - IO: [text] (overcomes: [obstacle])
    - IO: [text] (overcomes: [obstacle])
  
  Phase 2 (after Phase 1):
    - IO: [text] (overcomes: [obstacle])
  
  Phase 3 (after Phase 2):
    - IO: [text] (overcomes: [obstacle])

CRITICAL PATH: IO-1 → IO-3 → IO-5 → GOAL
QUICK WINS: IO-2, IO-4 (can start immediately, low effort)

NEXT STEP: Detail execution steps with /toc:tt
```

---

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Fix |
|-------------|---------------|-----|
| Obstacles are vague fears | "It might not work" is not actionable | Make each obstacle specific and evidence-based |
| IOs are too large | "Build new system" is a project, not a step | Break into smaller, achievable objectives |
| Everything is sequential | False dependencies slow implementation | Test: "Can we REALLY not do these in parallel?" |
| Missing obstacles | Optimism bias — "it'll be easy" | Ask skeptics: "Why do you think this won't work?" |
| IOs don't overcome obstacles | IO is a workaround, not a solution | Test: "With this IO achieved, is the obstacle GONE?" |

---

## Handoff

When used in the full TOC workflow (`/toc`):
- **Receives from FRT**: Validated injection + trims + known risks
- **Passes to TT**: Sequenced IOs as input for detailed transition steps

Output format for TT handoff:
```
PRT RESULTS FOR TT:
  Goal: [text]
  Implementation sequence:
    1. IO: [text] (no dependencies)
    2. IO: [text] (depends on #1)
    3. IO: [text] (depends on #1)
    4. IO: [text] (depends on #2 and #3)
  Critical path: [sequence]
  Risks to monitor: [from FRT]
```
