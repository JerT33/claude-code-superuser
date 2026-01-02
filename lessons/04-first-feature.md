# Chapter 4: Your First Feature

Now we're adding real functionality: configurable timer duration. This isn't a trivial fix—it's a feature with multiple valid approaches. Time to use **plan mode**.

## When to Use Plan Mode

In Chapter 3, we fixed trivial bugs and skipped planning. But for features like this:
- Multiple implementation approaches exist
- Architectural decisions need to be made
- You want to review the approach before Claude starts coding

## The Exercise

### Step 1: Enter Plan Mode

Type your request, then press `Shift+Tab` to send it in plan mode:

```
Add the ability to set a custom timer duration. Users should be able to specify how many minutes they want when starting a pomodoro.
```

(You can also prefix with `/plan` instead of using Shift+Tab)

This tells Claude to explore and plan *without* implementing.

### Step 2: Watch Claude Plan

Claude will:
1. Explore the codebase
2. Identify where changes are needed
3. Propose implementation options
4. Wait for your approval

You might see something like:

> **Option 1**: Positional argument
> - `python pomodoro.py start 15`
> - Simple, but ambiguous (15 what?)
>
> **Option 2**: Named argument
> - `python pomodoro.py start --minutes 15`
> - Clear, self-documenting
>
> I recommend Option 2...

### Step 3: Approve the Plan

Claude will prompt you to **auto accept** or **request approval**. Choose **request approval** so you can review each change as it's made.

Once you're happy with the plan, tell Claude to proceed.

Claude exits plan mode and implements the feature. As each edit comes up, you can reject it and provide feedback using option 3—this lets you steer the implementation without starting over.

### Step 4: Commit

```
commit these changes
```

## Test It

Run the app yourself:

```bash
python src/pomodoro.py start --minutes 5
```

The timer should now count down from 5 minutes (or whatever duration Claude implemented).

---

[Next: Chapter 5 - Make It Pretty →](05-make-it-pretty.md)

---

## Skills Learned

- [ ] Recognizing when to use plan mode
- [ ] Plan mode (Shift+Tab or `/plan`)
- [ ] Reviewing and approving plans
- [ ] Feature implementation workflow

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 3: Quick Wins](03-quick-wins.md) | [README](../README.md) | [Chapter 5: Make It Pretty](05-make-it-pretty.md) |
