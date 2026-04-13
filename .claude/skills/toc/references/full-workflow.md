# Full TOC Workflow — 4-Agent Pipeline Orchestration

## Overview

The full workflow chains all Thinking Process tools in sequence:

```
Problem → CRT → EC → FRT → PRT+TT → Action Plan
```

Each stage's output feeds into the next. The coordinator (main conversation context)
orchestrates 4 sequential agent calls, synthesizing outputs between stages.

## Why Sequential (Not Parallel)

Unlike review or meeting patterns where independent perspectives analyze the same input,
the TOC Thinking Processes form a strict dependency chain:

1. CRT must identify root causes BEFORE EC can resolve them
2. EC must produce injections BEFORE FRT can validate them
3. FRT must validate solutions BEFORE PRT can plan implementation
4. PRT must identify obstacles BEFORE TT can detail steps

Parallelization is not possible here — it would violate the logical flow.

---

## Stage 1: CRT Agent — Root Cause Analysis

**Model**: sonnet (structured analysis task)

```
Agent(
  description="CRT: Root cause analysis",
  model="sonnet",
  prompt="You are a Theory of Constraints analyst specializing in Current Reality Trees.

Read these files:
- .claude/skills/toc/references/crt-protocol.md
- .claude/skills/toc/references/output-format.md

PROBLEM:
{problem_text}

FORMAT: {format}
DEPTH: {depth}

Execute the full CRT protocol:
1. Extract UDEs from the problem description
2. Connect them via cause-effect chains (If...Then...)
3. Identify root causes (V-shape test)
4. Identify the core conflict

Output MUST include:
- CRT diagram in {format} format
- Numbered UDE list
- Root causes ranked by leverage
- Core conflict statement formatted for EC handoff:
  CORE CONFLICT FOR EC:
    Root cause: [text]
    Current behavior (D): [text]
    Alternative behavior (D'): [text]
    Why the conflict persists: [text]

Do NOT ask questions. Analyze with the information given."
)
```

**Coordinator action after Stage 1:**
- Extract the CORE CONFLICT FOR EC section from the output
- Extract root causes and UDE list for the final report
- Pass the core conflict to Stage 2

---

## Stage 2: EC Agent — Conflict Resolution

**Model**: opus (deep reasoning for assumption-breaking)

```
Agent(
  description="EC: Conflict resolution",
  model="opus",
  prompt="You are a Theory of Constraints analyst specializing in Evaporating Clouds.

Read these files:
- .claude/skills/toc/references/ec-protocol.md
- .claude/skills/toc/references/output-format.md

CONTEXT FROM CRT:
{crt_core_conflict}

{crt_summary_with_udes_and_root_causes}

FORMAT: {format}
DEPTH: {depth}

Execute the full EC protocol:
1. Construct the cloud (A, B, C, D, D') from the core conflict
2. Surface hidden assumptions (minimum 3 per arrow)
3. Break assumptions — find injection(s)
4. Rank injections by feasibility and impact

Output MUST include:
- Evaporating Cloud diagram in {format} format
- All assumptions by arrow
- Broken assumption(s) highlighted
- Recommended injection with assessment
- Handoff formatted for FRT:
  INJECTION FOR FRT VALIDATION:
    Injection: [text]
    Broken assumption: [text]
    Expected primary effect: [text]
    Concern areas: [list]

Do NOT ask questions. Analyze with the information given."
)
```

**Coordinator action after Stage 2:**
- Extract the INJECTION FOR FRT VALIDATION section
- Extract the evaporating cloud diagram and assumptions for the final report
- Pass the injection to Stage 3

---

## Stage 3: FRT Agent — Solution Validation

**Model**: opus (complex reasoning for side-effect projection)

```
Agent(
  description="FRT: Solution validation",
  model="opus",
  prompt="You are a Theory of Constraints analyst specializing in Future Reality Trees.

Read these files:
- .claude/skills/toc/references/frt-protocol.md
- .claude/skills/toc/references/output-format.md

CONTEXT FROM EC:
{ec_injection_section}

ORIGINAL PROBLEM CONTEXT:
{original_udes_from_crt}

FORMAT: {format}
DEPTH: {depth}

Execute the full FRT protocol:
1. State the injection and trace primary effects
2. Trace secondary and tertiary effects (map DEs to original UDEs)
3. Identify Negative Branch Reservations (NBRs)
4. Trim NBRs
5. Assess: PROCEED / PROCEED WITH CONDITIONS / RECONSIDER

Output MUST include:
- FRT diagram in {format} format
- DEs mapped to original UDEs
- NBRs with trims
- Overall assessment
- Handoff formatted for PRT:
  FRT RESULTS FOR PRT:
    Validated injection: [text]
    Required trims: [list]
    Implementation goal: [text]
    Known risks: [list]
    Success criteria: [text]

Do NOT ask questions. Analyze with the information given."
)
```

**Coordinator action after Stage 3:**

Check the assessment:
- **PROCEED or PROCEED WITH CONDITIONS**: Continue to Stage 4
- **RECONSIDER**: Report to user that the injection needs revision. Suggest running `/toc:ec` again with different constraint focus.

Extract FRT RESULTS FOR PRT section and pass to Stage 4.

---

## Stage 4: PRT+TT Agent — Implementation Planning

**Model**: sonnet (structured planning task)

```
Agent(
  description="PRT+TT: Implementation planning",
  model="sonnet",
  prompt="You are a Theory of Constraints analyst specializing in implementation planning (Prerequisite Trees and Transition Trees).

Read these files:
- .claude/skills/toc/references/prt-protocol.md
- .claude/skills/toc/references/tt-protocol.md
- .claude/skills/toc/references/output-format.md

CONTEXT FROM FRT:
{frt_results_section}

ORIGINAL PROBLEM:
{original_problem_text}

FORMAT: {format}
DEPTH: {depth}

Execute BOTH protocols:

PART 1 — Prerequisite Tree:
1. State the goal (validated injection + trims)
2. List obstacles
3. Define intermediate objectives (IOs)
4. Sequence by dependency

PART 2 — Transition Tree:
For each IO from the PRT:
1. Build the step-by-step chain: Reality → Action → Effect
2. Validate each step
3. Flag risk checkpoints

Output MUST include:
- PRT diagram in {format} format
- TT diagram(s) in {format} format
- Combined execution plan with timeline
- Quick wins (things that can start immediately)
- Risk checkpoints

Do NOT ask questions. Plan with the information given."
)
```

---

## Final Synthesis

After all 4 stages complete, the coordinator presents the consolidated report:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TOC THINKING PROCESSES — FULL ANALYSIS REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROBLEM: {original problem text}

━━━ STAGE 1: CURRENT REALITY TREE ━━━
What to change?

{CRT diagram}

Root Causes:
{ranked root cause list}

Core Conflict:
{conflict statement}

━━━ STAGE 2: EVAPORATING CLOUD ━━━
What to change TO?

{EC diagram}

Broken Assumption:
{broken assumption}

Injection:
{injection text}

━━━ STAGE 3: FUTURE REALITY TREE ━━━
Will it work?

{FRT diagram}

Assessment: {PROCEED / PROCEED WITH CONDITIONS / RECONSIDER}

Key DEs: {list}
Managed Risks: {NBRs + trims}

━━━ STAGE 4: IMPLEMENTATION PLAN ━━━
How to cause the change?

{PRT diagram}
{TT diagram(s)}

Action Plan:
{combined execution plan}

Quick Wins (start now):
{list}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The analysis identified [N] root causes behind [M] symptoms.
The core conflict is: {one-sentence conflict}.
The recommended injection is: {one-sentence injection}.
This injection resolves [X] of [M] symptoms with [Y] managed risks.

Immediate next steps:
1. {quick win 1}
2. {quick win 2}
3. {first major action}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Error Handling

### Stage Failure
If any agent fails or returns low-quality output:
- Use `SendMessage` to the same agent for clarification
- Provide the specific issue: "The root causes are too vague — make them more specific"
- Maximum 1 retry per stage

### RECONSIDER Assessment
If FRT returns RECONSIDER:
- Do NOT proceed to Stage 4
- Report to user: "The proposed injection has critical unresolved risks"
- Suggest: "Consider running `/toc:ec` again focusing on a different root cause"
- Present the partial analysis (CRT + EC + FRT) so the work is not lost

### Insufficient Problem Description
If CRT agent cannot extract enough UDEs:
- Coordinator uses AskUserQuestion to get more detail
- Re-runs Stage 1 with enriched input
