# Chapter 0: The Broken App

Before we touch Claude Code, let's see what we're working with.

## Run the App

```bash
python src/pomodoro.py start
```

Try the key bindings:
- Press `q` to quit
- Press `p` to pause (spoiler: it crashes)

<!-- SCREENSHOT: Terminal showing the timer with typos -->

## The Problems

- Typos everywhere in the output
- Timer display is off by one second
- Pause crashes the app
- Hardcoded 25 minutes (no way to change it)
- Ugly plain text output
- No history or stats
- No tests

Take a look at `src/pomodoro.py` if you want to see the mess. Don't fix anything yet.

## What You'll Build

By the end of this tutorial, this app will have:
- Clean output with colors and progress bar
- Working pause/resume
- Configurable duration
- Desktop notifications
- Session history and stats
- Full test suite
- Custom automation

Ready?

[Next: Chapter 1 - Global Setup →](01-global-setup.md)

---

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| - | [README](../README.md) | [Chapter 1: Global Setup](01-global-setup.md) |
