# toc-agents

Theory of Constraints — the complete Goldratt framework as Claude Code skills. No external dependencies.

## Commands

### Thinking Processes (Problem Solving)

| Command | Tool | Purpose |
|---------|------|---------|
| `/toc "problem"` | Full Workflow | CRT → EC → FRT → PRT → TT pipeline |
| `/toc:crt "problem"` | Current Reality Tree | Root cause analysis |
| `/toc:ec "conflict"` | Evaporating Cloud | Conflict resolution |
| `/toc:frt "injection"` | Future Reality Tree | Solution validation |
| `/toc:prt "goal"` | Prerequisite Tree | Obstacle identification |
| `/toc:tt "objectives"` | Transition Tree | Step-by-step action plan |

### Operations & Strategy

| Command | Tool | Purpose |
|---------|------|---------|
| `/toc:five-steps "system"` | Five Focusing Steps | Bottleneck identification & exploitation |
| `/toc:dbr "process"` | Drum-Buffer-Rope | Pull-based scheduling around constraint |
| `/toc:ccpm "project"` | Critical Chain PM | Project planning with shared buffers |
| `/toc:throughput "decision"` | Throughput Accounting | T/I/OE decision framework |
| `/toc:buy-in "change"` | Layers of Resistance | Overcome resistance to change |

## Rules

- Output diagrams in Mermaid by default, ASCII with `--format ascii`
- Every cause-effect arrow must pass the CLR (Categories of Legitimate Reservation) test
- Never present assumptions as facts — always mark assumptions explicitly
- When running full workflow, agents are sequential (each depends on prior output)
- Each sub-skill is standalone — can be invoked independently
- No external dependencies — pure Claude Code skills, no Python/npm required
