# Chapter 6: External Documentation

Now we're adding desktop notifications. Claude knows Python, but library APIs change. Let's learn to fetch up-to-date documentation.

## The Problem

You want:
- A desktop notification when the timer ends
- Maybe a sound too

Claude's training data has a cutoff. The library you need might have:
- Updated its API since then
- New features Claude doesn't know about
- Breaking changes Claude isn't aware of

## MCP Plugins

Claude Code supports **MCP (Model Context Protocol)** plugins that extend its capabilities. One of the most useful is **context7**—a plugin that fetches current library documentation.

## The Exercise

### Step 1: Check Available Plugins

```
What MCP plugins do you have available?
```

Claude will list its available plugins. Look for context7 or similar documentation tools.

### Step 2: Request the Feature

```
Add desktop notifications when the timer completes.
Use the context7 plugin to look up the current API for a Python
notification library, then implement it correctly.
```

Watch Claude:
1. Use the context7 plugin to fetch documentation
2. Read the current API
3. Implement with the correct, up-to-date syntax

<!-- SCREENSHOT: Claude fetching docs via context7 -->

### Step 3: Alternative - Web Fetch

If context7 isn't available, Claude can fetch documentation directly:

```
Look up the documentation for plyer (Python notification library)
and implement desktop notifications using the current API.
```

Claude will use web fetch to get the docs.

## Why This Matters

Without documentation fetching, you might get:

```python
# Claude's guess based on old training data
notify.send(message="Timer done")  # Wrong API!
```

With documentation fetching:

```python
# Correct current API
from plyer import notification
notification.notify(
    title='Pomodoro Complete',
    message='Time for a break!',
    timeout=10
)
```

## Add Sound Too

While we're at it:

```
Also add a sound when the notification appears.
Look up how to play a sound in Python cross-platform.
```

Claude might use `playsound`, `pygame`, or the system bell.

## Testing Notifications

```
Run a quick 5-second timer to test the notification
```

```bash
python src/pomodoro.py start --minutes 0.1
```

Wait for it... you should get a notification!

<!-- SCREENSHOT: Desktop notification appearing -->

## Handling Missing Dependencies

Claude might add imports for libraries you don't have. If the app crashes:

```
The app crashed because plyer isn't installed.
Add a requirements.txt file with all dependencies.
```

Then:

```bash
pip install -r requirements.txt
```

## Commit

```
/commit
```

## Common Documentation Sources

Claude can fetch from various sources:

| Source | Best For |
|--------|----------|
| context7 | Library API references |
| Web fetch | Documentation sites, tutorials |
| PyPI | Package info, version requirements |
| GitHub | Source code, examples, issues |

---

[Next: Chapter 7 - Context Mastery →](07-context-mastery.md)

---

## Skills Learned

- [ ] MCP plugins overview
- [ ] context7 for library documentation
- [ ] Web fetch for external resources
- [ ] Implementing with up-to-date APIs

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 5: Make It Pretty](05-make-it-pretty.md) | [README](../README.md) | [Chapter 7: Context Mastery](07-context-mastery.md) |
