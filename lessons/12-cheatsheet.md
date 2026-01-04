# Chapter 12: Cheat Sheet & Anti-Patterns

Congratulations—you've completed the tutorial. Here's your quick reference and a guide to common mistakes.

---

## Quick Reference

### Essential Commands

| Command | What It Does |
|---------|--------------|
| `claude` | Start Claude Code |
| `claude init` | Initialize project |
| `claude --resume` | Resume previous session |
| `claude --headless` | Non-interactive mode |
| `exit` or `Ctrl+C` | Exit Claude Code |

### Built-in Commands

| Command | What It Does |
|---------|--------------|
| `/clear` | Clear conversation context |
| `/compact` | Compress context |
| `/revert` | Revert to previous state |
| `/sessions` | List resumable sessions |
| `/resume` | Resume a previous session |
| `/help` | Show help |
| `/init` | Initialize project |
| `/model` | Switch models (Opus, Sonnet, Haiku) |
| `/plan` | View current plan |

### Custom Commands (Chapter 8)

| Command | What It Does |
|---------|--------------|
| `/commit` | Create a git commit |
| `/test` | Run tests |
| `/lint` | Run linter |

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Escape` | Cancel current operation |
| `Ctrl+C` | Exit Claude Code |
| `Up/Down` | Navigate history |

### Thinking Keywords

| Keyword | When to Use |
|---------|-------------|
| `think` | Moderate complexity, need more reasoning |
| `ultrathink` | High complexity, architecture decisions |

### Models (`/model`)

| Model | Best For | Cost |
|-------|----------|------|
| Haiku | Quick fixes, simple tasks | $ |
| Sonnet | Most coding tasks | $$ |
| Opus | Planning, architecture | $$$ |

**Pro tip:** Use Opus for planning, then switch to Sonnet for implementation.

---

## File Locations

| File | Purpose |
|------|---------|
| `~/.claude/CLAUDE.md` | Global instructions |
| `.claude/CLAUDE.md` | Project instructions |
| `.claude/settings.json` | Project settings |
| `.claude/commands/` | Custom slash commands |
| `.claude/skills/` | Custom skills |

---

## Task Classification

| Type | Examples | Workflow |
|------|----------|----------|
| **Trivial** | Typos, one-liners | Just do it |
| **Standard** | Features, bug fixes | Plan → Implement |
| **Complex** | Architecture changes | Full workflow + extra review |

---

## Context Management

| Range | Status | Action |
|-------|--------|--------|
| 0-30% | Plenty of room | Work freely |
| 30-60% | Normal | Monitor |
| 60-80% | Getting full | Consider compressing |
| 80%+ | Critical | Must manage |

---

## Anti-Patterns

### 1. Ignoring Context Until It's Too Late

**Wrong**: Work until Claude starts forgetting things, then panic.

**Right**: Monitor context percentage. Compress or start fresh proactively around 60-70%.

---

### 2. Not Committing Often Enough

**Wrong**: Implement an entire feature, then commit once at the end.

**Right**: Commit after each logical change. If something breaks, you can revert to a working state.

---

### 3. Over-Prompting Trivial Tasks

**Wrong**:
```
I need you to fix a typo in line 15 of src/pomodoro.py where it says
"Tmer" but it should say "Timer". Please read the file first, then
identify the exact location, then make the change, then show me a diff...
```

**Right**:
```
Fix the typo: "Tmer" -> "Timer"
```

---

### 4. Under-Prompting Complex Tasks

**Wrong**:
```
Add notifications
```

**Right**:
```
Add desktop notifications when the timer completes.
- Should work on Mac/Windows/Linux
- Include a sound if possible
- Make notifications optional via a --no-notify flag
```

---

### 5. Letting Claude Over-Engineer

**Wrong**: Accept Claude's suggestion to add a database, ORM, and analytics dashboard for a simple timer app.

**Right**: Push back. "That's over-engineered. Just use a JSON file."

---

### 6. Skipping the Planning Step

**Wrong**: "Add user authentication to the app" and let Claude immediately start coding.

**Right**: Ask Claude to propose options first. Authentication has many valid approaches—you should choose.

---

### 7. Not Using /resume

**Wrong**: Start fresh sessions every time, losing all context from previous work.

**Right**: Use `/resume` to continue strategic sessions. Plan in one, execute in others, resume to integrate.

---

### 8. Fighting Instead of Clarifying

**Wrong**:
```
No that's wrong. I told you to make it blue not red.
No, still wrong. Darker blue.
No, that's purple. I said BLUE.
```

**Right**:
```
Use hex color #2563eb for the progress bar.
```

Be specific. If Claude misunderstands, clarify with precision rather than arguing.

---

### 9. Ignoring the Global CLAUDE.md

**Wrong**: Never set up global instructions. Wonder why Claude doesn't follow your preferred workflow.

**Right**: Invest time in your Global CLAUDE.md. It pays dividends across every project.

---

### 10. Using --dangerously-skip-permissions Casually

**Wrong**: "Permission prompts are annoying, I'll just skip them all."

**Right**: Use allow lists for trusted commands. Reserve the nuclear option for CI/CD or when you truly understand the implications.

---

## Self-Assessment

You're a Claude Code Superuser if you can:

- [ ] Set up Global and Project CLAUDE.md files with effective instructions
- [ ] Classify tasks and use appropriate workflows
- [ ] Use extended thinking effectively
- [ ] Manage context proactively
- [ ] Use visual feedback with screenshots
- [ ] Create and manage branches and PRs
- [ ] Write and use custom skills and commands
- [ ] Orchestrate parallel work with `/resume`
- [ ] Configure permissions appropriately
- [ ] Run Claude headlessly for automation
- [ ] Recognize and avoid anti-patterns

---

## What's Next?

You've mastered Claude Code. Now:

1. **Apply it to real projects** - The skills transfer to any codebase
2. **Share with your team** - Help others level up
3. **Create team skills** - Encode your best practices
4. **Iterate on your Global CLAUDE.md** - Refine as you learn

---

## The Final App

Look at your Pomodoro app now:

```bash
python src/pomodoro.py start --minutes 25 --break-minutes 5 --daily-goal 8
```

From a buggy mess to a polished, tested, feature-rich tool.

You did that—with Claude Code as your pair.

---

## Navigation

| Previous | Up |
|----------|-----|
| [Chapter 11: Multi-Session Workflows](11-multi-session.md) | [README](../README.md) |

---

*Built with Claude Code. Obviously.*
