# Chapter 7: Context Mastery

By now, your context is probably getting heavy. Claude has read files, seen screenshots, made edits, run commands. Let's learn to manage this.

## Understanding Context

Claude has a finite context window—the total amount of text it can "remember" in a session. This includes:

- Your messages
- Claude's responses
- File contents Claude has read
- Command outputs
- Images (these take a lot of space)

When context fills up, Claude starts forgetting earlier parts of the conversation.

## Monitoring Context

### The Context Percentage

Watch your context indicator. It tells you how full the window is.

<!-- SCREENSHOT: Context percentage indicator -->

| Range | Status | Action |
|-------|--------|--------|
| 0-30% | Plenty of room | Work freely |
| 30-60% | Normal | Keep an eye on it |
| 60-80% | Getting full | Consider managing |
| 80%+ | Critical | Must manage now |

## Context Management Techniques

### 1. Compress Context

When context gets high, ask Claude to summarize:

```
Summarize what we've accomplished in this session so far,
then we can compress the context.
```

Or use the compact command:

```
/compact
```

This tells Claude to summarize the conversation, reducing token usage while preserving important information.

### 2. Clear Context

For a fresh start:

```
/clear
```

This wipes the conversation. Use when:
- You're starting a completely new task
- Context is critically full
- The conversation has gone off track

**Warning**: After `/clear`, Claude forgets everything from the session. It still has your CLAUDE.md files, but not the conversation history.

### 3. Revert Context

Made a mistake? Went down a wrong path?

```
/revert
```

This rolls back to a previous state in the conversation. Useful when:
- Claude's last change broke something
- You want to try a different approach
- You accidentally approved something you shouldn't have

<!-- SCREENSHOT: Using /revert -->

## When to Start Fresh vs. Continue

### Continue When:
- You're working on related tasks
- Claude has valuable context (codebase knowledge, your preferences)
- Context is under 60%

### Start Fresh When:
- Switching to completely unrelated work
- Context is over 80%
- The conversation is confused or off-track
- Claude keeps making the same mistake

## The Exercise

### Step 1: Check Your Context

```
How much context are we using? What are the biggest items?
```

### Step 2: Compress

If over 50%:

```
/compact
```

Watch the context percentage drop.

### Step 3: Practice Revert

Make an intentional mistake:

```
Delete the format_time function from pomodoro.py
```

After Claude does it:

```
/revert
```

The deletion is undone.

## Pro Tips

### Image Cost

Images consume a lot of context. If you've shared many screenshots:
- Consider starting fresh for non-visual work
- Summarize visual feedback in words when possible

### Large Files

Reading large files fills context fast. For big codebases:
- Ask Claude to read specific functions, not whole files
- Use search to find relevant code instead of reading everything

### Long Sessions

For long sessions:
- Periodically compress
- Commit frequently (so you can recover if needed)
- Start fresh for major task switches

---

[Next: Chapter 8 - Make It Pretty →](08-make-it-pretty.md)

---

## Skills Learned

- [ ] Context percentage monitoring
- [ ] Compressing context manually (`/compact`)
- [ ] Clearing context (`/clear`)
- [ ] Revert context (`/revert`)
- [ ] When to start fresh vs continue

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 6: Testing](06-testing.md) | [README](../README.md) | [Chapter 8: Make It Pretty](08-make-it-pretty.md) |
