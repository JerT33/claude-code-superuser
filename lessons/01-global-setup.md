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

---

[Next: Chapter 2 - Project Init →](02-project-init.md)

---

## Skills Learned

- [ ] Global CLAUDE.md creation
- [ ] Task scope classification (trivial/standard/complex)
- [ ] Planning-first workflow
- [ ] Clarify-before-acting principle

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 0: The Broken App](00-the-broken-app.md) | [README](../README.md) | [Chapter 2: Project Init](02-project-init.md) |
