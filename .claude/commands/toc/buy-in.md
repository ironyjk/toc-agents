---
name: toc:buy-in
description: "Layers of Resistance — systematically overcome resistance to change using Goldratt's 6-layer buy-in process"
argument-hint: "[Change: <text>] [--format mermaid|ascii] [--depth shallow|deep]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **Change**: The proposed change that faces resistance. The entire argument text IS the change if not explicitly labeled.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.
- **Depth**: `shallow` (default) or `deep`. Set by `--depth`.

If Change is missing, use AskUserQuestion:

```
header: "Change"
question: "What change are you trying to implement? Who is resisting it, and what reasons do they give?"
```

## Execution

1. Read the protocol file:
   ```
   .claude/skills/toc/references/buy-in-protocol.md
   ```

2. Read the output format specification:
   ```
   .claude/skills/toc/references/output-format.md
   ```

3. Execute the Buy-in protocol:
   - Diagnose which layer(s) of resistance are active
   - For each layer, build the argument that overcomes it
   - Map the persuasion sequence
   - Present talking points for each layer

4. Present the result with:
   - Resistance diagnosis (which layers are active)
   - Persuasion strategy for each layer
   - Talking points and evidence needed
   - Sequence for the conversation
