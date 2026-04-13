---
name: toc:ec
description: "Evaporating Cloud — resolve conflicts by surfacing and breaking hidden assumptions"
argument-hint: "[Conflict: <text>] [--format mermaid|ascii] [--depth shallow|deep]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **Conflict**: The dilemma, tradeoff, or conflict to resolve. Look for patterns like "X vs Y", "on one hand...on the other", or any tension between two positions. If not explicitly stated, the entire argument text IS the conflict.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.
- **Depth**: `shallow` (default, 3-5 assumptions per arrow) or `deep` (8-10 per arrow). Set by `--depth`.

If Conflict is missing or too vague to identify two opposing positions, use AskUserQuestion:

```
header: "Conflict"
question: "Describe the conflict or dilemma you want to resolve. What are the two things you feel you can't do at the same time?"
```

## Execution

1. Read the protocol file:
   ```
   .claude/skills/toc/references/ec-protocol.md
   ```

2. Read the output format specification:
   ```
   .claude/skills/toc/references/output-format.md
   ```

3. Execute the Evaporating Cloud protocol against the Conflict:
   - Phase 1: Construct the Cloud (A, B, C, D, D')
   - Phase 2: Surface hidden assumptions (3-5 per arrow minimum)
   - Phase 3: Break assumptions → find injection(s)
   - Phase 4: Render output in requested format

4. Present the result with:
   - The Evaporating Cloud diagram
   - All assumptions listed by arrow
   - Broken assumption(s) highlighted
   - Injection(s) with feasibility assessment
