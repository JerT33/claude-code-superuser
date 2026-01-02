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

Run the app yourself in another terminal:

```bash
python src/pomodoro.py help
```

The output should now be spelled correctly.

## Commit the Fix

Now let's commit this fix:

```
commit these changes
```

Claude will run `git status`, `git diff`, draft a commit message, and create the commit.

## Fix the Timer Bug

### Step 1: Ask Claude to Fix the Off-by-One

```
Fix the off-by-one error in the timer display
```

Claude should find the bug in `format_time()` where it subtracts 1 from seconds incorrectly.

### Step 2: Commit

```
commit these changes
```

## Fix the Crash

### Step 1: Fix the Pause Handler

```
Fix the handle_pause function so pressing 'p' doesn't crash the app
```

The function references `remaning` (typo) which doesn't exist. Claude should fix it to properly pause the timer.

### Step 2: Commit

```
commit these changes
```

## The App So Far

Run the app yourself to verify your fixes:

```bash
python src/pomodoro.py start
```

Press `p` to test pause, `q` to quit. It should no longer crash, display correct spelling, and show accurate time.

Still ugly. Still hardcoded. But functional.

---

[Next: Chapter 4 - Your First Feature →](04-first-feature.md)

---

## Skills Learned

- [ ] Recognizing trivial tasks (skip planning)
- [ ] Basic prompting for fixes
- [ ] Committing with natural language
- [ ] Incremental commits

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 2: Project Init](02-project-init.md) | [README](../README.md) | [Chapter 4: Your First Feature](04-first-feature.md) |
