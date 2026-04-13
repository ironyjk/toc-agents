---
name: toc:dbr
description: "Drum-Buffer-Rope — design a pull-based scheduling system around the constraint"
argument-hint: "[Process: <text>] [--format mermaid|ascii] [--depth shallow|deep] [--optimize]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **Process**: The production/service process to optimize. Describe the flow of work, key steps, and where bottlenecks occur. The entire argument text IS the process if not explicitly labeled.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.
- **Depth**: `shallow` (default) or `deep`. Set by `--depth`.

If Process is missing, use AskUserQuestion:

```
header: "Process"
question: "Describe the process or workflow you want to optimize. What are the main steps? Where does work pile up? What's the end-to-end flow?"
```

## Execution

1. Read the protocol file:
   ```
   .claude/skills/toc/references/dbr-protocol.md
   ```

2. Read the output format specification:
   ```
   .claude/skills/toc/references/output-format.md
   ```

3. Execute the DBR protocol:
   - Identify the Drum (constraint that sets the pace)
   - Size the Buffer (time buffer before the constraint)
   - Design the Rope (signal from constraint to release new work)
   - Define buffer management zones (green/yellow/red)

4. Present the result with:
   - Process flow diagram with Drum, Buffer, and Rope marked
   - Specific scheduling rules
   - Buffer management dashboard design

## OR-Tools Solver Mode (--optimize)

When `--optimize` is specified and the user provides **specific jobs with quantities and due dates**:

1. Extract job data and stage capacities from the description
2. Create JSON and run: `python solvers/dbr_scheduler.py --data toc_dbr.json`
3. Present optimized schedule with drum start times (rope release order)
4. Also run: `python solvers/buffer_sim.py --data toc_buffer.json` for buffer sizing
