# Chapter 9: Testing & Hooks

Time to add tests and automate quality checks. We'll use Claude Code hooks to enforce standards.

## Why Testing Matters

The off-by-one bug from Chapter 0? A simple unit test would have caught it. Let's make sure new bugs can't sneak in.

## The Exercise: Add Tests

### Step 1: Ask Claude to Add Tests

```
Add unit tests for the pomodoro app using pytest.
Focus on:
- format_time function
- Duration argument parsing
- Stats calculation

Create a tests/ directory with test files.
```

Claude will:
1. Create the test directory structure
2. Write test files
3. Add test cases for each function

<!-- SCREENSHOT: Claude creating test files -->

### Step 2: Run the Tests

```
Run the tests and show me the results
```

```bash
pytest tests/ -v
```

All tests should pass (assuming Claude wrote them correctly for the current implementation).

### Step 3: Test-Driven Bug Fix

Let's verify tests catch bugs:

```
Temporarily break the format_time function
(add that off-by-one error back), then run the tests.
```

The tests should fail. Then:

```
Fix it and run tests again.
```

Now they pass. This is the value of tests.

## Hooks

Hooks are shell commands that run automatically at certain points. They're configured in your project or global settings.

### Types of Hooks

| Hook | When It Runs |
|------|--------------|
| Pre-commit | Before git commits |
| Post-commit | After git commits |
| Pre-push | Before git pushes |
| File change | When files are modified |

### Setting Up a Pre-Commit Hook

```
Set up a hook that runs pytest before every commit.
If tests fail, the commit should be blocked.
```

Claude will configure a pre-commit hook that:
1. Runs `pytest tests/`
2. Blocks the commit if any tests fail
3. Allows the commit if tests pass

### Test the Hook

```
Make a change that breaks a test, then try to commit.
```

The commit should be blocked with test failure output.

```
Fix the change, then commit again.
```

Now it works.

<!-- SCREENSHOT: Hook blocking a commit due to failed tests -->

### Adding a Linter Hook

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

With tests and hooks, you now have:

1. **Unit tests** - Verify code works correctly
2. **Pre-commit hook** - Prevents committing broken code
3. **Linter hook** - Maintains code style

This catches problems before they become bugs in production.

## Commit

```
/commit
```

The commit hook runs, tests pass, commit succeeds.

---

[Next: Chapter 10 - Git Workflows →](10-git-workflows.md)

---

## Skills Learned

- [ ] Writing tests with Claude
- [ ] Hooks overview
- [ ] Pre-commit hooks
- [ ] Post-change hooks
- [ ] Quality automation

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 8: Persistence & Stats](08-persistence-stats.md) | [README](../README.md) | [Chapter 10: Git Workflows](10-git-workflows.md) |
