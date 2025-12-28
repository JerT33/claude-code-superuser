# Chapter 2: Project Init & Orientation

Now let's initialize Claude Code in the Pomodoro project and get oriented with the codebase.

## Initialize the Project

### Step 1: Run claude init

In the project directory:

```bash
cd claude-code-superuser
claude init
```

This creates a `.claude/` directory with project-specific settings.

<!-- SCREENSHOT: Terminal showing claude init output -->

### Step 2: Create Project CLAUDE.md

Now ask Claude to create a project-specific CLAUDE.md:

```
Create a project CLAUDE.md file at .claude/CLAUDE.md for this Pomodoro timer app.
Include:
- Brief description of the app (a CLI pomodoro timer)
- The main file location (src/pomodoro.py)
- Note that this is a learning project for Claude Code skills
- How to run the app: python src/pomodoro.py start
```

Claude will create the file. This gives Claude project-specific context every time you work on this codebase.

## Explore the Codebase

### Step 3: Ask Claude to Explore

Now let's see Claude's exploration in action:

```
Explore this codebase. What does the app do? What's the structure?
What problems do you notice in the code?
```

Watch what happens:
- Claude reads files
- The **context percentage** in your terminal increases
- Claude summarizes its findings

<!-- SCREENSHOT: Claude exploring with context percentage visible -->

### Understanding Context Percentage

Notice the percentage indicator (usually in your status bar or prompt). This shows how much of Claude's context window is being used.

- **Low (0-30%)**: Plenty of room, Claude can read more files
- **Medium (30-60%)**: Normal working range
- **High (60-80%)**: Getting full, consider managing context soon
- **Critical (80%+)**: Need to compress or clear

For now, just notice it exists. We'll cover context management in Chapter 7.

### Step 4: Run the App with Claude

Ask Claude to run the app:

```
Run the pomodoro app and show me the output
```

Claude will execute:

```bash
python src/pomodoro.py start
```

<!-- SCREENSHOT: Claude running the app, showing buggy output -->

Now ask:

```
Try running the pause command
```

Watch it crash. Claude can now see the problem firsthand.

## What Claude Knows Now

After this exploration, Claude has:
- Read the project CLAUDE.md (project context)
- Read the source code (implementation details)
- Run the app (seen actual behavior)
- Seen the crash (confirmed the bug)

This context persists in your session. Claude remembers all of this as you continue.

## Try It: Ask Questions

Practice asking Claude questions about the codebase:

```
What's causing the timer to show the wrong time?
```

```
Why does the pause command crash?
```

```
List all the typos in the output strings
```

Claude can answer these because it's already explored the code.

---

[Next: Chapter 3 - Quick Wins →](03-quick-wins.md)

---

## Skills Learned

- [ ] `claude init`
- [ ] Project CLAUDE.md creation
- [ ] Context percentage awareness
- [ ] Bash commands (running the app)
- [ ] Codebase exploration with Claude

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 1: Global Setup](01-global-setup.md) | [README](../README.md) | [Chapter 3: Quick Wins](03-quick-wins.md) |
