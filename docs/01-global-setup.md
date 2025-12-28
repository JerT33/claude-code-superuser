# Chapter 1: Global Setup & Best Practices

Before we touch the project, let's configure Claude Code with a planning-first workflow that will apply to **all** your projects.

## Why Global Configuration?

Claude Code reads instructions from a file at `~/.claude/CLAUDE.md`. These instructions shape how Claude approaches every task:
- How it plans before implementing
- When it asks clarifying questions
- How it breaks down complex work

Setting this up correctly is the highest-leverage thing you can do.

## The Exercise

You're going to use Claude Code to set up its own configuration. Meta, right?

### Step 1: Start Claude Code

```bash
claude
```

### Step 2: Ask Claude to Create Your Global Config

Tell Claude:

```
Create a global CLAUDE.md file at ~/.claude/CLAUDE.md using the template
from examples/global-claude-md-template.md in this repo. Read the template
first, then create the file exactly as specified.
```

Claude will:
1. Read the template
2. Create the `~/.claude` directory if needed
3. Write the file

<!-- SCREENSHOT: Claude creating the global CLAUDE.md file -->

### Step 3: Verify It Worked

Ask Claude:

```
Read ~/.claude/CLAUDE.md and summarize what workflow it defines
```

Claude should describe the planning-first workflow you just installed.

## Understanding the Workflow

The global config you just installed defines this workflow:

### Task Classification

Before any task, classify it:
- **Trivial**: Typos, single-line fixes → Just do it
- **Standard**: Features, bug fixes → Follow full workflow
- **Complex**: Architecture changes → Full workflow + extra scrutiny

### The Planning-First Workflow

For standard and complex tasks:

1. **Clarify** - Ask questions before acting
2. **Discover** - Scan the codebase for context
3. **Plan** - Propose 2-3 options with tradeoffs
4. **Implement** - Step by step after approval
5. **Test** - Run tests, verify no regressions
6. **Validate** - Quality review with subagent

### Scope Discipline

- Only fix what was requested
- Flag adjacent issues, don't fix them without asking
- Resist the urge to refactor "while you're in there"

## Why This Matters

Without these instructions, Claude might:
- Jump straight to coding without understanding the problem
- Over-engineer simple fixes
- Make changes you didn't ask for
- Skip planning on complex tasks

With them, Claude becomes a disciplined collaborator that checks in with you at the right moments.

## Configure Allow Settings (Optional)

You can also configure global allow settings to reduce permission prompts for commands you trust:

```bash
claude config set allowedCommands "git status, git diff, git log, python, pytest"
```

This tells Claude these commands are always safe to run without asking.

---

[Next: Chapter 2 - Project Init →](02-project-init.md)

---

## Skills Learned

- [ ] Global CLAUDE.md creation
- [ ] Task scope classification (trivial/standard/complex)
- [ ] Planning-first workflow
- [ ] Clarify-before-acting principle
- [ ] Configure global allow settings

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 0: The Broken App](00-the-broken-app.md) | [README](../README.md) | [Chapter 2: Project Init](02-project-init.md) |
