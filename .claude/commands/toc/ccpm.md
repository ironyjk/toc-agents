---
name: toc:ccpm
description: "Critical Chain Project Management — plan projects with shared buffers instead of padded task estimates"
argument-hint: "[Project: <text>] [--format mermaid|ascii] [--depth shallow|deep]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **Project**: The project to plan or analyze. Describe key tasks, dependencies, resources, and deadline. The entire argument text IS the project if not explicitly labeled.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.
- **Depth**: `shallow` (default) or `deep`. Set by `--depth`.

If Project is missing, use AskUserQuestion:

```
header: "Project"
question: "Describe the project you want to plan. What are the main tasks? What depends on what? What resources are shared? What's the deadline?"
```

## Execution

1. Read the protocol file:
   ```
   .claude/skills/toc/references/ccpm-protocol.md
   ```

2. Read the output format specification:
   ```
   .claude/skills/toc/references/output-format.md
   ```

3. Execute the CCPM protocol:
   - Identify the Critical Chain (longest resource-constrained path)
   - Cut task estimates by 50% (remove hidden safety)
   - Add Project Buffer (end of critical chain)
   - Add Feeding Buffers (where non-critical chains join)
   - Design buffer management (green/yellow/red tracking)

4. Present the result with:
   - Project network diagram with critical chain highlighted
   - Buffer sizes and placement
   - Staggering rules for multi-project environments
   - Buffer management dashboard
