# Chapter 2: Project Init & Orientation

Now let's initialize Claude Code in the Pomodoro project and get oriented with the codebase.

## Initialize the Project

### Step 1: Run /init

In your existing Claude session, type:

```
/init
```

Claude will walk you through creating a `.claude/` directory and a project CLAUDE.md file. This gives Claude project-specific context every time you work on this codebase.

<!-- SCREENSHOT: Terminal showing claude init output -->

## Explore the Codebase

### Step 2: Ask Claude to Explore

Now let's see Claude's exploration in action:

```
Explore this codebase. What does the app do? What's the structure?
What problems do you notice in the code?
```

Watch what happens:
- Claude reads files
- The **context percentage** in your terminal increases
- Claude summarizes its findings

If you need to stop Claude mid-operation, press `Escape`.

<!-- SCREENSHOT: Claude exploring with context percentage visible -->

### Understanding Context Percentage

Notice the percentage indicator (usually in your status bar or prompt). This shows how much of Claude's context window is being used.

- **Low (0-30%)**: Plenty of room, Claude can read more files
- **Medium (30-60%)**: Normal working range
- **High (60-80%)**: Getting full, consider managing context soon
- **Critical (80%+)**: Need to compress or clear

For now, just notice it exists. We'll cover context management in Chapter 7.

---

[Next: Chapter 3 - Quick Wins →](03-quick-wins.md)

---

## Skills Learned

- [ ] `/init` command
- [ ] Project CLAUDE.md creation
- [ ] Context percentage awareness
- [ ] Codebase exploration

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 1: Global Setup](01-global-setup.md) | [README](../README.md) | [Chapter 3: Quick Wins](03-quick-wins.md) |
