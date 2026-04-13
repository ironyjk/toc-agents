---
name: toc:tt
description: "Transition Tree — create a step-by-step execution plan with current reality, action, and expected effect for each step"
argument-hint: "[Objectives: <text>] [--format mermaid|ascii] [--depth shallow|deep]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **Objectives**: The intermediate objectives or goals to achieve. Can be a list from PRT or a single objective. The entire argument text IS the objectives if not explicitly labeled.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.
- **Depth**: `shallow` (default, 3-5 steps per IO) or `deep` (6-10 steps per IO). Set by `--depth`.

If Objectives are missing, use AskUserQuestion:

```
header: "Objectives"
question: "What objectives do you need to achieve? List the key milestones or intermediate goals — I'll create a step-by-step action plan for each."
```

## Execution

1. Read the protocol file:
   ```
   .claude/skills/toc/references/tt-protocol.md
   ```

2. Read the output format specification:
   ```
   .claude/skills/toc/references/output-format.md
   ```

3. Execute the Transition Tree protocol:
   - Phase 1: List objectives to achieve
   - Phase 2: For each objective, build the transition chain
   - Phase 3: Validate each step's logic
   - Phase 4: Render output in requested format

4. Present the result with:
   - The TT diagram for each objective
   - Step-by-step action plan with current reality → action → effect
   - Dependencies and sequencing
   - Risk checkpoints
