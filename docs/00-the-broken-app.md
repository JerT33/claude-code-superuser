# Chapter 0: The Broken App

Before we touch Claude Code, let's see what we're working with.

## Run the App

```bash
cd claude-code-superuser
python src/pomodoro.py start
```

Watch it for a few seconds. Notice anything wrong?

<!-- SCREENSHOT: Terminal showing the timer running with typos visible -->

## The Problems

Let's catalog everything wrong with this app:

### 1. Typos Everywhere

Look at the output:
- "Staring" instead of "Starting"
- "Pomdoro" instead of "Pomodoro"
- "Tmer" instead of "Timer"
- "minuts" instead of "minutes"
- "brak" instead of "break"
- ...and more

### 2. Timer Shows Wrong Time

Watch the seconds. They're off by one. When the timer should show `24:59`, it shows `24:58`. This is a bug in the code.

### 3. It Crashes

Try running:

```bash
python src/pomodoro.py pause
```

You'll get a `NameError`. The pause function references a variable that doesn't exist.

### 4. Hardcoded Everything

Want a 15-minute timer? Too bad. It's 25 minutes or nothing. The duration is hardcoded with no way to change it.

### 5. Ugly Output

Plain text. No colors. No progress bar. No ASCII art tomato. Just ugly.

### 6. No Persistence

Complete a pomodoro? The app has no memory. No history. No stats. No streaks.

### 7. No Tests

Zero tests. The off-by-one bug would have been caught with even basic testing.

## Take a Look at the Code

Open `src/pomodoro.py` and skim through it. You'll see:
- The typos are in the strings
- The off-by-one is in `format_time()`
- The crash is in `pause_timer()` (references undefined `remaining`)
- Everything is hardcoded

Don't fix anything yet. That's what Claude Code is for.

## What You'll Build

By the end of this tutorial, this app will have:
- Clean, professional output
- Accurate timer with configurable duration
- Beautiful CLI with colors and progress bar
- Desktop notifications and sound
- Session history and statistics
- Break timer between pomodoros
- Daily goal setting
- Full test suite
- Automated quality checks

And more importantly, you'll know how to use Claude Code to build anything.

## Ready?

[Next: Chapter 1 - Global Setup →](01-global-setup.md)

---

## Skills Learned

None yet - this chapter is just setup and motivation.

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| - | [README](../README.md) | [Chapter 1: Global Setup](01-global-setup.md) |
