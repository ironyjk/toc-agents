---
name: toc:five-steps
description: "Five Focusing Steps — identify and exploit the system's constraint (bottleneck)"
argument-hint: "[System: <text>] [--format mermaid|ascii] [--depth shallow|deep]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **System**: The system, process, or organization to analyze for constraints. The entire argument text IS the system description if not explicitly labeled.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.
- **Depth**: `shallow` (default, focus on the primary constraint) or `deep` (analyze secondary constraints and what happens after elevating). Set by `--depth`.

If System is missing, use AskUserQuestion:

```
header: "System"
question: "Describe the system or process you want to analyze. What is its goal? What are the main steps or resources involved? Where do you feel things slow down or get stuck?"
```

## Execution

1. Read the protocol file:
   ```
   .claude/skills/toc/references/five-steps-protocol.md
   ```

2. Read the output format specification:
   ```
   .claude/skills/toc/references/output-format.md
   ```

3. Execute the Five Focusing Steps protocol:
   - Step 1: IDENTIFY the constraint
   - Step 2: EXPLOIT the constraint
   - Step 3: SUBORDINATE everything else
   - Step 4: ELEVATE the constraint
   - Step 5: Check — has the constraint moved? REPEAT

4. Present the result with:
   - System flow diagram showing the constraint
   - Specific actions for each of the 5 steps
   - Expected throughput improvement
   - Warning: what becomes the NEXT constraint after elevation
