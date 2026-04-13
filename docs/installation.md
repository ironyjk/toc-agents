# Installation Guide

## Prerequisites

- [Claude Code](https://claude.ai/claude-code) installed and configured
- That's it. No Python, Node.js, or other dependencies needed.

## Method 1: Use Directly (Recommended for Trying Out)

```bash
git clone https://github.com/ironyjk/toc-agents.git
cd toc-agents
claude
```

Then run any command:
```
/toc:ec "We need to ship faster but we also need to maintain quality"
```

## Method 2: Copy Into Your Project

If you want TOC tools available in your existing project:

```bash
# Clone toc-agents somewhere
git clone https://github.com/ironyjk/toc-agents.git /tmp/toc-agents

# Copy commands into your project
cp -r /tmp/toc-agents/.claude/commands/toc.md your-project/.claude/commands/
cp -r /tmp/toc-agents/.claude/commands/toc/ your-project/.claude/commands/

# Copy skill references
mkdir -p your-project/.claude/skills/toc
cp -r /tmp/toc-agents/.claude/skills/toc/ your-project/.claude/skills/
```

Your project structure should look like:
```
your-project/
├── .claude/
│   ├── commands/
│   │   ├── toc.md              # Main entry point
│   │   └── toc/
│   │       ├── ec.md           # Evaporating Cloud
│   │       ├── crt.md          # Current Reality Tree
│   │       ├── frt.md          # Future Reality Tree
│   │       ├── prt.md          # Prerequisite Tree
│   │       ├── tt.md           # Transition Tree
│   │       ├── five-steps.md   # Five Focusing Steps
│   │       ├── dbr.md          # Drum-Buffer-Rope
│   │       ├── ccpm.md         # Critical Chain PM
│   │       ├── throughput.md   # Throughput Accounting
│   │       └── buy-in.md       # Layers of Resistance
│   └── skills/
│       └── toc/
│           └── references/
│               ├── core-theory.md
│               ├── output-format.md
│               ├── ec-protocol.md
│               ├── crt-protocol.md
│               ├── frt-protocol.md
│               ├── prt-protocol.md
│               ├── tt-protocol.md
│               ├── five-steps-protocol.md
│               ├── dbr-protocol.md
│               ├── ccpm-protocol.md
│               ├── throughput-protocol.md
│               ├── buy-in-protocol.md
│               └── full-workflow.md
├── your-existing-files...
```

## Verifying Installation

Run Claude Code in your project directory and try:

```
/toc:ec "test conflict: speed vs quality"
```

You should see an Evaporating Cloud analysis with a Mermaid diagram.

## Updating

```bash
cd /path/to/toc-agents
git pull
# Re-copy if using Method 2
```

## Troubleshooting

### Commands not showing up

Make sure the `.claude/commands/toc.md` file exists in your project root. Claude Code discovers skills from this directory.

### "Protocol file not found"

The skill references must be at `.claude/skills/toc/references/`. Check that you copied the entire `skills/toc/` directory structure.

### Full workflow is slow

The full pipeline (`/toc "problem"`) runs 4 sequential agents. Each takes 30-60 seconds. Total: 2-4 minutes. For faster results, use individual tools directly (e.g., `/toc:ec`, `/toc:crt`).
