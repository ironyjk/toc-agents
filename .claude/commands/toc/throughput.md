---
name: toc:throughput
description: "Throughput Accounting — evaluate decisions using T, I, OE instead of traditional cost accounting"
argument-hint: "[Decision: <text>] [--format mermaid|ascii]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **Decision**: The business decision or investment to evaluate. The entire argument text IS the decision if not explicitly labeled.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.

If Decision is missing, use AskUserQuestion:

```
header: "Decision"
question: "What decision are you trying to evaluate? Describe the options, costs, and expected outcomes."
```

## Execution

1. Read the protocol file:
   ```
   .claude/skills/toc/references/throughput-protocol.md
   ```

2. Read the output format specification:
   ```
   .claude/skills/toc/references/output-format.md
   ```

3. Execute the Throughput Accounting protocol:
   - Calculate T (Throughput), I (Investment), OE (Operating Expense)
   - Compare options using T, I, OE impact
   - Apply constraint-based decision rules
   - Present recommendation

4. Present the result with:
   - T/I/OE analysis for each option
   - Decision matrix
   - Impact on constraint throughput
   - Recommendation with rationale
