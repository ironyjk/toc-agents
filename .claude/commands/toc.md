---
name: toc
description: "Theory of Constraints Thinking Processes — full analysis pipeline or individual tool routing"
argument-hint: "[Problem: <text>] [--tool ec|crt|frt|prt|tt|five-steps|dbr|ccpm|throughput|buy-in] [--format mermaid|ascii] [--depth shallow|deep]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract from $ARGUMENTS:

- **Problem**: The situation, conflict, or challenge to analyze. The entire argument text IS the problem if not explicitly labeled.
- **Tool**: Optional. Routes to a specific sub-tool: `ec`, `crt`, `frt`, `prt`, `tt`, `five-steps`, `dbr`, `ccpm`, `throughput`, `buy-in`. Set by `--tool`.
- **Format**: `mermaid` (default) or `ascii`. Set by `--format`.
- **Depth**: `shallow` (default) or `deep`. Set by `--depth`.

## Routing

### Single Tool Mode (--tool specified)

If `--tool` is specified, route to the corresponding sub-skill:

| --tool | Invoke |
|--------|--------|
| `ec` | Read `.claude/skills/toc/references/ec-protocol.md` and execute |
| `crt` | Read `.claude/skills/toc/references/crt-protocol.md` and execute |
| `frt` | Read `.claude/skills/toc/references/frt-protocol.md` and execute |
| `prt` | Read `.claude/skills/toc/references/prt-protocol.md` and execute |
| `tt` | Read `.claude/skills/toc/references/tt-protocol.md` and execute |
| `five-steps` | Read `.claude/skills/toc/references/five-steps-protocol.md` and execute |
| `dbr` | Read `.claude/skills/toc/references/dbr-protocol.md` and execute |
| `ccpm` | Read `.claude/skills/toc/references/ccpm-protocol.md` and execute |
| `throughput` | Read `.claude/skills/toc/references/throughput-protocol.md` and execute |
| `buy-in` | Read `.claude/skills/toc/references/buy-in-protocol.md` and execute |

Always also read `.claude/skills/toc/references/output-format.md` for rendering.

### Full Workflow Mode (no --tool)

If no `--tool` is specified, run the full 4-agent pipeline.

Read the orchestration protocol:
```
.claude/skills/toc/references/full-workflow.md
```

Read the output format:
```
.claude/skills/toc/references/output-format.md
```

### Missing Problem

If Problem is missing or too vague, use AskUserQuestion:

```
header: "Problem"
question: "Describe the problem, conflict, or challenge you want to analyze. Be as specific as possible — what symptoms are you seeing? What decisions are you struggling with?"
```

After receiving the answer, determine whether to suggest a specific tool or run the full workflow:

| Signal in user's response | Suggested tool |
|--------------------------|----------------|
| "X vs Y", "dilemma", "tradeoff", "can't do both" | `/toc:ec` |
| "why does this keep happening", "root cause", multiple symptoms | `/toc:crt` |
| "will this work", "what could go wrong", "validate" | `/toc:frt` |
| "how do we get there", "what's blocking us" | `/toc:prt` |
| "step by step", "action plan", "what to do first" | `/toc:tt` |
| "bottleneck", "constraint", "throughput" | `/toc:five-steps` |
| "scheduling", "WIP", "lead time", "flow" | `/toc:dbr` |
| "project plan", "late projects", "multitasking" | `/toc:ccpm` |
| "should we invest", "accept order", "make vs buy", "pricing" | `/toc:throughput` |
| "resistance", "buy-in", "convince", "pushback", "stakeholder" | `/toc:buy-in` |
| Complex/unclear — multiple aspects | Full workflow (CRT→EC→FRT→PRT→TT) |
