# Expansion Packs

Optional custom commands that enhance your Claude Code workflow.

## Available Packs

| Pack | Command | Description |
|------|---------|-------------|
| [prompt-evaluation](prompt-evaluation/) | `/evaluate-prompts` | Rate and analyze your prompts with improvement suggestions |
| [session-wrap-up](session-wrap-up/) | `/quit` | Gracefully end sessions with summaries and learning capture |

## Installation

Each pack is self-contained. See the README in each folder for install instructions.

General pattern:
```bash
cp <pack-folder>/<command>.md ~/.claude/commands/
```

## Creating Your Own

Commands are markdown files in `~/.claude/commands/`. The filename becomes the command name.

Structure:
```markdown
---
description: Short description shown in command list
allowed-tools: Tool1, Tool2  # Optional: restrict which tools the command can use
---

# Command Title

Instructions for Claude to follow...
```
