# Chapter 3: Quick Wins

Time to fix some bugs. These are trivial tasks—perfect for learning basic Claude Code commands without overthinking.

## Recognizing Trivial Tasks

Remember the task classification from your Global CLAUDE.md:

- **Trivial**: Typos, single-line fixes, simple questions → Skip to implementation

The bugs we're fixing here are trivial. We don't need a planning phase. We just fix them.

## Fix the Typos

### Step 1: Ask Claude to Fix Typos

```
Fix all the typos in the output strings in src/pomodoro.py.
Things like "Tmer" should be "Timer", "Pomdoro" should be "Pomodoro", etc.
```

Watch Claude:
1. Read the file (if not already in context)
2. Identify all typos
3. Make the edits
4. Show you what changed

<!-- SCREENSHOT: Claude fixing typos with diff view -->

### Step 2: Verify the Fix

```
Run the app and show me the output
```

The output should now be spelled correctly.

## Commit the Fix

### The /commit Command

Now let's commit this fix:

```
/commit
```

Claude will:
1. Run `git status` to see changes
2. Run `git diff` to see what changed
3. Draft a commit message
4. Create the commit

<!-- SCREENSHOT: Claude running /commit -->

**Important**: Claude writes the commit message based on the actual changes. You don't need to describe what you did—Claude already knows.

## Fix the Timer Bug

### Step 1: Ask Claude to Fix the Off-by-One

```
Fix the off-by-one error in the timer display
```

Claude should find the bug in `format_time()` where it subtracts 1 from seconds incorrectly.

### Step 2: Commit

```
/commit
```

Another clean commit.

## Fix the Crash

### Step 1: Fix the Pause Handler

```
Fix the handle_pause function so pressing 'p' doesn't crash the app
```

The function references `remaning` (typo) which doesn't exist. Claude should fix it to properly pause the timer.

### Step 2: Commit

```
/commit
```

## Keyboard Shortcuts

While working, try these shortcuts:

| Shortcut | Action |
|----------|--------|
| `Escape` | Cancel current operation |
| `Ctrl+C` | Exit Claude Code |
| `Up/Down` | Navigate command history |

**Pro tip**: If Claude is generating something you don't want, hit `Escape` to stop it immediately.

## Check Your Progress

You've now made 3 commits:
1. Fixed typos
2. Fixed timer display
3. Fixed pause crash

Run:

```
Show me the git log with commit messages
```

Claude will run `git log` and show your progress.

<!-- SCREENSHOT: Git log showing three commits -->

## The App So Far

Run the app again:

```bash
python src/pomodoro.py start
```

It should:
- Display correct spelling
- Show accurate time
- Not crash on pause (though pause may not do much yet)

Still ugly. Still hardcoded. But functional.

---

[Next: Chapter 4 - Your First Feature →](04-first-feature.md)

---

## Skills Learned

- [ ] Recognizing trivial tasks (skip planning)
- [ ] Basic prompting for fixes
- [ ] `/commit` command
- [ ] Keyboard shortcuts (Escape, etc.)
- [ ] Incremental commits

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 2: Project Init](02-project-init.md) | [README](../README.md) | [Chapter 4: Your First Feature](04-first-feature.md) |
