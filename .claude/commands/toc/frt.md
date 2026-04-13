---
name: toc:frt
description: "Future Reality Tree — validate a proposed solution by tracing its effects and identifying negative side-effects"
argument-hint: "[Injection: <text>] [--format mermaid|ascii] [--depth shallow|deep]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **Injection**: The proposed solution, change, or idea to validate. Can be a single action or a set of related changes. The entire argument text IS the injection if not explicitly labeled.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.
- **Depth**: `shallow` (default, trace 2-3 levels of effects) or `deep` (trace 4-5 levels, more NBRs). Set by `--depth`.

If Injection is missing, use AskUserQuestion:

```
header: "Proposed Solution"
question: "What change or action are you considering? Describe what you plan to do — I'll trace its likely effects and identify potential problems."
```

## Execution

1. Read the protocol file:
   ```
   .claude/skills/toc/references/frt-protocol.md
   ```

2. Read the output format specification:
   ```
   .claude/skills/toc/references/output-format.md
   ```

3. Execute the Future Reality Tree protocol:
   - Phase 1: State the injection and its expected primary effects
   - Phase 2: Trace secondary and tertiary effects (positive DEs)
   - Phase 3: Identify Negative Branch Reservations (NBRs)
   - Phase 4: Trim NBRs with additional conditions
   - Phase 5: Render output in requested format

4. Present the result with:
   - The FRT diagram showing DEs, NBRs, and trims
   - Assessment: Does the injection achieve the desired objective?
   - List of NBRs and their trims
   - Overall recommendation (proceed / proceed with conditions / reconsider)
