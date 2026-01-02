# Chapter 8: Persistence & Stats

The timer works beautifully now. But every pomodoro vanishes into the void. Let's add history and statistics—while practicing scope discipline.

## Scope Discipline

This is a larger feature. Your Global CLAUDE.md warns against scope creep:

> Only fix what was requested. If you discover adjacent issues during implementation, note them briefly, ask before fixing them.

We'll practice this. Our goal: basic persistence and stats. Not a full analytics dashboard.

## The Exercise

### Step 1: Define the Scope

Be specific about what you want:

```
Add session history and statistics to the pomodoro app:

1. Save completed pomodoros to a JSON file (~/.pomodoro_history.json)
2. Add a "stats" command that shows:
   - Total pomodoros completed
   - Total time focused
   - Current streak (consecutive days with at least 1 pomodoro)

Keep it simple. No databases, no complex analytics.
```

### Step 2: Watch for Scope Creep

Claude might suggest:
- "Should I add weekly/monthly breakdowns?"
- "Want me to add charts?"
- "I could add category tagging for different tasks"

Your answer: **No.** Stick to the scope.

```
Just the basics for now. We can add more later.
```

<!-- SCREENSHOT: Claude asking about additional features -->

### Step 3: Review the Implementation

Claude will likely create:
- A function to save completed pomodoros
- A JSON file structure
- A stats command

Watch for over-engineering:
- Did Claude create unnecessary abstractions?
- Is there a class hierarchy where a simple dict would work?
- Are there features you didn't ask for?

If so:

```
This is over-engineered. Simplify it:
- Use a simple list of dicts, not a class
- Remove the [feature you didn't ask for]
```

## Multi-File Changes

This feature touches multiple parts of the code:
- New save/load functions
- Modification to `run_timer()` to save on complete
- New `stats` command
- Updated help text

Watch how Claude:
1. Plans the changes across files
2. Implements them in logical order
3. Keeps changes consistent

## Flagging Adjacent Issues

During implementation, Claude might notice:
- "The help text is inconsistent with the commands"
- "The config could be refactored"
- "There's duplicated code that could be extracted"

The correct response from Claude (per your Global CLAUDE.md):
> I noticed [issue]. Should I fix this now, or focus on the current task?

The correct answer from you: **Focus on current task.**

```
Note it for later, but let's finish this feature first.
```

## Testing the Feature

### Complete a Pomodoro

```bash
python src/pomodoro.py start --minutes 0.1
```

### Check the History File

```
Show me what's in ~/.pomodoro_history.json
```

### View Stats

```bash
python src/pomodoro.py stats
```

You should see your stats.

## Commit

```
/commit
```

## Avoiding Over-Engineering

Common over-engineering patterns Claude might attempt:

| Over-Engineered | Simple Alternative |
|-----------------|-------------------|
| SQLite database | JSON file |
| ORM with models | Dict/list |
| Abstract base class | Plain function |
| Config system | Hardcoded reasonable defaults |
| Plugin architecture | Direct implementation |

For a CLI timer, simple is better.

---

[Next: Chapter 9 - Testing & Hooks →](09-testing-hooks.md)

---

## Skills Learned

- [ ] Scope discipline (stay focused)
- [ ] Multi-file changes
- [ ] Flagging adjacent issues without fixing
- [ ] Avoiding over-engineering

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 7: Context Mastery](07-context-mastery.md) | [README](../README.md) | [Chapter 9: Testing & Hooks](09-testing-hooks.md) |
