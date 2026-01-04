# Chapter 9: Hooks

Claude Code hooks let you run shell commands automatically when Claude performs certain actions. This is powerful for enforcing standards and automating workflows.

## Types of Hooks

| Hook | When It Runs |
|------|--------------|
| `PreToolUse` | Before Claude uses a tool (Write, Edit, Bash, etc.) |
| `PostToolUse` | After Claude uses a tool |
| `Notification` | When Claude sends a notification |
| `Stop` | Conditions that stop Claude's execution |

## The Exercise

### Create a Branch

```
Create a branch called feature/hooks
```

### Step 1: View Current Hooks

```
Show me my current Claude Code hooks configuration
```

Claude will check your `.claude/settings.json` or settings for any configured hooks.

### Step 2: Add a Pre-Tool Hook

Let's add a hook that runs before any file edit:

```
Add a Claude Code hook that runs a linter check before any Edit or Write tool use.
If the linter finds errors in the file being edited, warn me.
```

This creates a `PreToolUse` hook that runs before Claude modifies files.

### Step 3: Add a Post-Tool Hook

```
Add a hook that automatically runs tests after Claude edits any Python file.
```

This creates a `PostToolUse` hook that ensures tests pass after changes.

## Hook Configuration

Hooks are configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "tool": "Edit",
        "command": "ruff check $FILE"
      }
    ],
    "PostToolUse": [
      {
        "tool": "Edit",
        "command": "pytest tests/ -q"
      }
    ]
  }
}
```

Ask Claude to explain your configuration:

```
Explain my current hooks and what each one does.
```

## Practical Hook Examples

### Prevent Editing Certain Files

```
Add a hook that blocks editing any file in the /config directory without confirmation.
```

### Auto-Format on Save

```
Add a hook that runs black formatter after any Python file is written.
```

### Notify on Long Operations

```
Add a notification hook that alerts me if any Bash command takes longer than 30 seconds.
```

## When to Use Hooks

**Good use cases:**
- Running linters/formatters automatically
- Running tests after changes
- Preventing accidental edits to sensitive files
- Logging Claude's actions

**Avoid:**
- Hooks that slow down every operation
- Complex logic (use skills instead)

## Commit and PR

Once you're happy with your hooks setup:

```
commit these changes
```

```
create a pull request
```

Merge the PR, then return to main:

```
switch to main and pull latest
```

---

[Next: Chapter 10 - Advanced Config →](10-advanced-config.md)

---

## Skills Learned

- [ ] Claude Code hook types
- [ ] PreToolUse hooks
- [ ] PostToolUse hooks
- [ ] Hook configuration in settings
- [ ] Practical hook patterns

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 8: Custom Automation](08-custom-automation.md) | [README](../README.md) | [Chapter 10: Advanced Config](10-advanced-config.md) |
