# Session Wrap-Up

A comprehensive command for ending your Claude Code sessions gracefully.

## What It Does

1. Summarizes what was accomplished
2. Evaluates your prompts
3. Lists unfinished items
4. Saves a session log to `~/.claude/sessions/`
5. Proposes learnings to remember for future sessions
6. Saves approved learnings to `~/.claude/rules/learnings.md`

## Prerequisites

```bash
mkdir -p ~/.claude/sessions ~/.claude/rules
touch ~/.claude/rules/learnings.md
```

Also install the `prompt-evaluation` expansion pack (this command uses it).

## Install

Copy the command file to your Claude commands directory:

```bash
cp quit.md ~/.claude/commands/
```

## Usage

```
/quit
```

Run at the end of any session.
