# Chapter 12: Multi-Session Workflows

This is where Claude Code becomes a true power tool. You'll orchestrate parallel work across multiple sessions, using `/resume` to coordinate.

## The Scenario

You need to add two features:
1. **Break timer** - Rest periods between pomodoros
2. **Daily goals** - Set and track daily pomodoro targets

Instead of doing them sequentially, you'll:
- Plan both in a main session
- Implement each in separate sessions
- Resume the main session to integrate

This mirrors real-world workflows where you might plan with your team, work independently, then regroup.

## The Exercise

### Part 1: Planning Session (Main)

Start a fresh Claude session:

```bash
claude
```

Plan both features:

```
I need to add two features to the pomodoro app:

1. Break timer - After each pomodoro, prompt for a 5-minute break.
   Should be skippable. Show different visuals during break.

2. Daily goals - Let users set a daily target (e.g., 8 pomodoros).
   Show progress toward goal. Persist across sessions.

Think through both features. Give me an implementation plan for each
that I can hand off to separate implementation sessions.
```

Claude will produce detailed plans for both features.

**Important**: Note your session ID. You can see it with:

```
/sessions
```

Or note it from the terminal display.

<!-- SCREENSHOT: Session ID visible -->

Write it down: `Session ID: __________`

### Part 2: Close the Main Session

Exit Claude:

```
exit
```

Or press `Ctrl+C`.

The main session is now closed—but its context is preserved.

### Part 3: Feature A Session

Start a new Claude session:

```bash
claude
```

This is a fresh session. Implement the break timer:

```
Implement a break timer feature for the pomodoro app:
- After each pomodoro ends, offer a 5-minute break
- Make break duration configurable with --break-minutes
- Show blue progress bar during break (different from work)
- Allow skipping with 's' key
```

Work through the implementation. Commit when done:

```
commit these changes
```

Exit this session:

```
exit
```

### Part 4: Feature B Session

Start another new session:

```bash
claude
```

Implement daily goals:

```
Implement a daily goals feature for the pomodoro app:
- Add --daily-goal flag to set target pomodoros for the day
- Track progress in the history file
- Show progress when starting: "Today: 3/8 pomodoros"
- Celebrate when goal is reached
```

Work through it. Commit:

```
commit these changes
```

Exit:

```
exit
```

### Part 5: Resume Main Session

Now the magic. Resume your original planning session:

```bash
claude --resume
```

Or start Claude and use:

```
/resume
```

Select your original session from the list (or enter the ID you noted).

<!-- SCREENSHOT: Selecting a session to resume -->

**Claude remembers everything from the planning session.** The feature plans, the context, the discussion.

### Part 6: Integration

Now tell Claude what happened:

```
I implemented both features in separate sessions:
- Break timer is done (with --break-minutes flag)
- Daily goals is done (with --daily-goal flag)

Both are committed. Help me verify the implementations
match the plans we discussed, and make sure they work
together correctly.
```

Claude will:
1. Read the current code (which now has both features)
2. Compare against the plans from this session's context
3. Check for integration issues
4. Suggest any needed fixes

This is the power of `/resume`—you maintained strategic context while tactical work happened elsewhere.

## Why This Matters

### Real-World Parallel Work

In practice, you might:
- Plan a sprint in one session
- Implement features in focused sessions
- Resume the planning session for standup/review

### Context Preservation

The main session remembers:
- The overall plan
- Decisions you made
- Trade-offs discussed
- The "why" behind features

Individual sessions focus on execution.

### Multi-Agent Patterns

You can also spawn parallel agents within a session:

```
Use agents to implement both features in parallel:
- One agent for break timer
- One agent for daily goals
```

Claude creates subagents that work simultaneously.

## Custom Agents

For specialized tasks, you can create custom agents:

```
Create a QA agent that:
- Reviews code changes for bugs
- Checks test coverage
- Validates documentation
- Reports issues in a structured format
```

Then use it:

```
Run the QA agent on the last 3 commits.
```

## Session Management

### View Sessions

```
/sessions
```

Shows recent sessions you can resume.

### Clean Up

Old sessions eventually expire. For important ones:

```
Save a summary of this session for future reference.
```

---

[Next: Chapter 13 - Cheat Sheet & Anti-Patterns →](13-cheatsheet.md)

---

## Skills Learned

- [ ] Session management (`/sessions`)
- [ ] `/resume` for parallel orchestration
- [ ] Planning in one session, executing in others
- [ ] Context preservation across time
- [ ] Multi-agent patterns
- [ ] Creating custom agents

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 11: Advanced Config](11-advanced-config.md) | [README](../README.md) | [Chapter 13: Cheat Sheet](13-cheatsheet.md) |
