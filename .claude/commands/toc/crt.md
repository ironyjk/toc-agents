---
name: toc:crt
description: "Current Reality Tree — find root causes by mapping cause-effect chains from observable symptoms"
argument-hint: "[Problem: <text>] [--format mermaid|ascii] [--depth shallow|deep]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **Problem**: The situation, symptoms, or undesirable effects to analyze. Can be a list of specific UDEs or a general problem description. The entire argument text IS the problem if not explicitly labeled.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.
- **Depth**: `shallow` (default, 5-8 UDEs, 1-2 root causes) or `deep` (10-15 UDEs, 2-4 root causes). Set by `--depth`.

If Problem is missing, use AskUserQuestion:

```
header: "Problem"
question: "Describe the situation you want to analyze. What symptoms or problems are you seeing? List as many specific issues as you can."
```

## Execution

1. Read the protocol file:
   ```
   .claude/skills/toc/references/crt-protocol.md
   ```

2. Read the output format specification:
   ```
   .claude/skills/toc/references/output-format.md
   ```

3. Execute the Current Reality Tree protocol:
   - Phase 1: Gather and validate UDEs
   - Phase 2: Connect UDEs via cause-effect chains (If...Then...)
   - Phase 3: Identify root causes (V-shape test)
   - Phase 4: Identify core conflict (for EC handoff)
   - Phase 5: Render output in requested format

4. Present the result with:
   - The CRT diagram
   - Numbered list of UDEs
   - Root causes ranked by leverage (how many UDEs each explains)
   - Core conflict statement (ready for `/toc:ec` if user wants to continue)
