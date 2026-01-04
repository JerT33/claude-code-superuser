# Chapter 10: Hooks

Hooks are shell commands that run automatically at certain points. They let you automate quality checks and enforce standards.

## Types of Hooks

| Hook | When It Runs |
|------|--------------|
| Pre-commit | Before git commits |
| Post-commit | After git commits |
| Pre-push | Before git pushes |
| File change | When files are modified |

## The Exercise

### Step 1: Set Up a Pre-Commit Hook

```
Set up a hook that runs pytest before every commit.
If tests fail, the commit should be blocked.
```

Claude will configure a pre-commit hook that:
1. Runs `pytest tests/`
2. Blocks the commit if any tests fail
3. Allows the commit if tests pass

### Step 2: Test the Hook

```
Make a change that breaks a test, then try to commit.
```

The commit should be blocked with test failure output.

```
Fix the change, then commit again.
```

Now it works.

<!-- SCREENSHOT: Hook blocking a commit due to failed tests -->

### Step 3: Add a Linter Hook

```
Add a hook that runs a Python linter (ruff or flake8) on changed files.
Warn but don't block if there are issues.
```

This gives you feedback about code style without being too strict.

## Hook Configuration

Hooks are typically configured in:
- `.claude/hooks.json` for Claude Code specific hooks
- `.pre-commit-config.yaml` for pre-commit framework
- Git hooks in `.git/hooks/`

Ask Claude where your hooks are configured:

```
Show me where the hooks are configured and explain each one.
```

## Quality Automation

With tests (from Chapter 6) and hooks, you now have:

1. **Unit tests** - Verify code works correctly
2. **Pre-commit hook** - Prevents committing broken code
3. **Linter hook** - Maintains code style

This catches problems before they become bugs in production.

## Commit

Once you're happy with your hooks setup:

```
commit these changes
```

---

[Next: Chapter 11 - Advanced Config →](11-advanced-config.md)

---

## Skills Learned

- [ ] Hook types and when they run
- [ ] Pre-commit hooks
- [ ] Linter hooks
- [ ] Hook configuration locations
- [ ] Quality automation

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 9: Custom Automation](09-custom-automation.md) | [README](../README.md) | [Chapter 11: Advanced Config](11-advanced-config.md) |
