# Chapter 13: Advanced Configuration

Time for the power-user settings: permissions, headless mode, and team configuration.

## Permission System

Claude Code asks for permission before:
- Running bash commands
- Writing files
- Making network requests

This is a safety feature. But for trusted operations, it can slow you down.

### Understanding Permissions

When Claude wants to run `python src/pomodoro.py`, you'll see:

```
Claude wants to run: python src/pomodoro.py
Allow? [y/n/always]
```

Options:
- `y` - Allow this once
- `n` - Deny
- `always` - Allow this command always (adds to allow list)

### Allow Lists

You've already configured some allow lists. View them:

```
Show me my current allow list settings (global and project).
```

#### Global Allow List

Applies to all projects:

```bash
claude config set allowedCommands "git status, git diff, git log, python, pytest"
```

#### Project Allow List

In `.claude/settings.json`:

```json
{
  "allowedCommands": [
    "python src/pomodoro.py",
    "pytest tests/",
    "ruff check"
  ]
}
```

### The Nuclear Option

```bash
claude --dangerously-skip-permissions
```

This skips **all** permission checks. Use only when:
- Running trusted automation
- In CI/CD pipelines
- You fully understand the risks

**Never use this with untrusted prompts or in production environments with sensitive access.**

## Headless/CI Mode

Claude Code can run without human interaction. Perfect for:
- CI/CD pipelines
- Automated testing
- Batch operations

### Basic Headless Usage

```bash
echo "Run the tests and report results" | claude --headless
```

Or with a file:

```bash
claude --headless < prompt.txt
```

### CI Pipeline Example

In GitHub Actions:

```yaml
- name: Review PR with Claude
  run: |
    echo "Review the changes in this PR for bugs and style issues" | \
    claude --headless --dangerously-skip-permissions
```

### Headless Options

| Flag | Purpose |
|------|---------|
| `--headless` | Non-interactive mode |
| `--output json` | JSON output for parsing |
| `--max-tokens 1000` | Limit response length |

## Team Configuration

Setting up Claude Code for a team:

### Shared Project Settings

The `.claude/` directory can be committed:

```
.claude/
  CLAUDE.md          # Project context
  settings.json      # Allowed commands, preferences
  commands/          # Custom slash commands
  skills/            # Team skills
```

Commit this so everyone has the same configuration.

### Template for New Team Members

Create a setup guide:

```
Create a CONTRIBUTING.md that explains:
1. How to set up Claude Code for this project
2. Required global CLAUDE.md contents
3. Recommended allow list settings
4. Our custom commands and skills
```

### Security Considerations

For teams, consider:

1. **Don't allow dangerous commands globally**
   - Restrict `rm`, `curl`, `wget` to specific contexts

2. **Review custom skills**
   - Skills can run arbitrary commands
   - Review before committing to shared repo

3. **Rotate API keys**
   - If using API access, rotate keys regularly

4. **Audit logs**
   - Consider logging Claude's actions for review

## The Exercise

### Set Up Project Permissions

```
Configure the project allow list for our pomodoro app:
- Allow running the app
- Allow running tests
- Allow linting
- Deny anything else until explicitly allowed
```

### Test Headless Mode

```bash
echo "What is the current state of the pomodoro app? List features implemented." | \
claude --headless
```

### Create Team Documentation

```
Create a .claude/README.md that explains our Claude Code setup
for new team members joining this project.
```

---

[Next: Chapter 14 - Cheat Sheet & Anti-Patterns →](14-cheatsheet.md)

---

## Skills Learned

- [ ] Project allow settings
- [ ] Permission system deep dive
- [ ] `--dangerously-skip-permissions` (and warnings)
- [ ] Headless/CI mode
- [ ] Team configuration

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 12: Multi-Session Workflows](12-multi-session.md) | [README](../README.md) | [Chapter 14: Cheat Sheet & Anti-Patterns](14-cheatsheet.md) |
