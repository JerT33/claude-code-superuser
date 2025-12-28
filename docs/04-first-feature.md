# Chapter 4: Your First Feature

Now we're adding real functionality: configurable timer duration. This is a **standard task**—time to use the full planning workflow.

## Standard Task Workflow

This isn't a typo fix. We're adding a feature that could be implemented multiple ways. Your Global CLAUDE.md tells Claude to:

1. Clarify requirements
2. Explore the codebase
3. Propose 2-3 options
4. Wait for approval
5. Implement step by step

Let's see this in action.

## The Exercise

### Step 1: Request the Feature

```
Add the ability to set a custom timer duration. Users should be able to
specify how many minutes they want when starting a pomodoro.
```

### Step 2: Watch Claude's Workflow

If your Global CLAUDE.md is set up correctly, Claude should:

**Clarify** (maybe):
> "Should the duration be passed as a command line argument, or should there be a config file?"

If Claude asks, answer:
```
Command line argument. Like: python pomodoro.py start 15
```

**Plan** with options:
> Here are some approaches:
>
> **Option 1**: Positional argument
> - `python pomodoro.py start 15`
> - Simple, but 15 what? Seconds? Minutes?
>
> **Option 2**: Named argument
> - `python pomodoro.py start --minutes 15`
> - Clear, self-documenting
>
> **Option 3**: Short flag
> - `python pomodoro.py start -m 15`
> - Shorter but less discoverable
>
> I recommend Option 2...

<!-- SCREENSHOT: Claude presenting options -->

### Step 3: Approve and Implement

Pick an option (or let Claude proceed with its recommendation):

```
Go with option 2, the named argument
```

Claude implements the feature.

## Extended Thinking

For more complex decisions, you can ask Claude to think harder:

### The `think` Keyword

Add "think" to your prompt:

```
think about edge cases for the duration argument - what if someone
passes 0, or a negative number, or a string?
```

Claude will spend more time reasoning through the problem before responding.

### The `ultrathink` Keyword

For even deeper analysis:

```
ultrathink about the architecture for this timer - if we later want to
add break timers, repeating pomodoros, and stats, how should we structure
the code now to support that?
```

This uses more tokens but produces more thorough analysis.

## Model Switching

Different models have different strengths:

| Model | Best For | Cost |
|-------|----------|------|
| **Haiku** | Simple edits, quick fixes | $ |
| **Sonnet** | Most coding tasks | $$ |
| **Opus** | Complex architecture, deep analysis | $$$ |

For this feature:
- Use **Sonnet** (default) for implementation
- Use **Opus** if you want deep architectural thinking

You can switch models in settings or by starting Claude with a specific model flag.

## Cost Awareness

Extended thinking and larger models cost more. For a simple feature like this:
- `think` is probably sufficient
- `ultrathink` with Opus is overkill
- Save the heavy thinking for complex architectural decisions

## Commit the Feature

```
/commit
```

Claude should create a commit message that describes the new feature.

## Test It

```bash
python src/pomodoro.py start --minutes 5
```

The timer should now count down from 5 minutes.

Try edge cases:
```bash
python src/pomodoro.py start --minutes 0
python src/pomodoro.py start --minutes -5
python src/pomodoro.py start --minutes abc
```

Does it handle them gracefully? If not, that's a future improvement.

---

[Next: Chapter 5 - Make It Pretty →](05-make-it-pretty.md)

---

## Skills Learned

- [ ] Standard task workflow in action
- [ ] Planning with 2-3 options
- [ ] Extended thinking (`think` keyword)
- [ ] Deep thinking (`ultrathink` keyword)
- [ ] Model switching (haiku/sonnet/opus)
- [ ] Cost awareness

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 3: Quick Wins](03-quick-wins.md) | [README](../README.md) | [Chapter 5: Make It Pretty](05-make-it-pretty.md) |
