---
name: toc:prt
description: "Prerequisite Tree — identify obstacles between current state and goal, then find intermediate objectives to overcome each"
argument-hint: "[Goal: <text>] [--format mermaid|ascii] [--depth shallow|deep]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **Goal**: The objective to achieve. Can be an injection from EC/FRT or any desired end state. The entire argument text IS the goal if not explicitly labeled.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.
- **Depth**: `shallow` (default, 3-5 obstacles) or `deep` (6-10 obstacles). Set by `--depth`.

If Goal is missing, use AskUserQuestion:

```
header: "Goal"
question: "What do you want to achieve? Describe the desired end state — I'll identify the obstacles in your way and how to overcome each one."
```

## Execution

1. Read the protocol file:
   ```
   .claude/skills/toc/references/prt-protocol.md
   ```

2. Read the output format specification:
   ```
   .claude/skills/toc/references/output-format.md
   ```

3. Execute the Prerequisite Tree protocol:
   - Phase 1: State the goal clearly
   - Phase 2: List obstacles preventing the goal
   - Phase 3: Define intermediate objectives (IOs) to overcome each obstacle
   - Phase 4: Sequence the IOs (dependencies)
   - Phase 5: Render output in requested format

4. Present the result with:
   - The PRT diagram showing obstacles, IOs, and their sequence
   - Prioritized list of obstacles with their IOs
   - Suggested implementation sequence
   - Ready for `/toc:tt` to detail the execution steps
