# Chapter 4: Your First Feature

Now we're adding real functionality: configurable timer duration. This isn't a trivial fix—it's a feature with multiple valid approaches. Time to use **plan mode**.

## When to Use Plan Mode

In Chapter 3, we fixed trivial bugs and skipped planning. But for features like this:
- Multiple implementation approaches exist
- Architectural decisions need to be made
- You want to review the approach before Claude starts coding

## Extended Thinking

For complex tasks, you can ask Claude to think more deeply by including keywords in your prompt:

| Keyword | When to Use |
|---------|-------------|
| `think` | Moderate complexity, need more reasoning |
| `ultrathink` | High complexity, architecture decisions |

Example:

```
Think through how to add custom timer duration. Consider different approaches and their tradeoffs.
```

For very complex features, you can combine with plan mode:

```
Ultrathink about the best way to implement session persistence with statistics tracking.
```

Claude will spend more time reasoning before responding, resulting in better solutions for complex problems.

## Model Selection

Different models excel at different tasks. Use `/model` to switch:

```
/model
```

This shows available models and lets you switch.

| Model | Best For |
|-------|----------|
| **Opus** | Planning, architecture decisions |
| **Sonnet** | Implementation, most coding tasks |

**Pro tip:** Use Opus for planning, then switch to Sonnet when the plan looks good and you're ready to implement.

```
/model opus
```

Plan your feature with Opus, then:

```
/model sonnet
```

Switch to Sonnet for the actual coding.

## Scope Discipline

When implementing features, stay focused:

- **Only build what's requested** - Don't add "nice to have" extras
- **Resist over-engineering** - A simple solution that works beats a complex one
- **Flag, don't fix** - If you notice unrelated issues, note them for later

If Claude suggests additional features ("Should I also add X?"), the default answer is **no**:

```
Just the basics for now. We can add more later.
```

This keeps implementations clean and prevents scope creep.

## The Exercise

### Step 1: Enter Plan Mode

Type your request, then press `Shift+Tab` to send it in plan mode:

```
Add the ability to set a custom timer duration. Users should be able to specify how many minutes they want when starting a pomodoro. Give me a couple of different options with pros/cons of each.
```

(Once a plan is created you can use `/plan` to view the plan anytime)

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

The timer should now count down from 5 minutes.

---

[Next: Chapter 5 - Git Workflows →](05-git-workflows.md)

---

## Skills Learned

- [ ] Recognizing when to use plan mode
- [ ] Plan mode (Shift+Tab and `/plan`)
- [ ] Extended thinking (`think`, `ultrathink`)
- [ ] Model selection (`/model`)
- [ ] Scope discipline
- [ ] Reviewing and approving plans

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 3: Quick Wins](03-quick-wins.md) | [README](../README.md) | [Chapter 5: Git Workflows](05-git-workflows.md) |
