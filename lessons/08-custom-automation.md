# Chapter 8: Custom Automation

You've been typing things like "commit these changes" throughout the tutorial. Now let's create shortcuts so you can just type `/commit` instead.

## Slash Commands vs Skills

Claude Code supports two types of custom automation:

| Type | What It Is | When to Use |
|------|------------|-------------|
| **Slash Command** | Quick shortcut for a prompt | Simple, frequent tasks |
| **Skill** | More complex automation with full prompts | Multi-step workflows |

## Creating a Slash Command

### Step 1: Create a Commit Command

Let's start with the most useful one—a `/commit` command:

```
Create a slash command called /commit that commits all staged changes with a descriptive message.
```

Claude will create a command configuration. Now instead of typing "commit these changes", you can just:

```
/commit
```

### Step 2: Create More Commands

Let's add a few more useful ones:

```
Create a /test command that runs pytest with verbose output.
```

```
Create a /lint command that runs ruff check on the src directory.
```

```
Create a /run command that starts the pomodoro timer with default settings.
```

## Creating a Skill

Skills are more powerful. They're full prompts that execute complex workflows.

### Step 1: Create a Release Skill

```
Create a skill called "release" that:
1. Runs all tests
2. Bumps the version number
3. Updates CHANGELOG.md
4. Creates a git tag
5. Pushes to origin with tags

The skill should ask for the version bump type (major, minor, patch).
```

Claude creates a skill file with the full prompt and logic.

<!-- SCREENSHOT: A skill file -->

### Step 2: Use the Skill

```
/release
```

Claude executes the multi-step workflow, asking for input where needed.

## Skill File Structure

A skill file typically contains:

```markdown
# Release Skill

## Inputs
- bump_type: major | minor | patch

## Steps
1. Run test suite
2. Calculate new version from bump_type
3. Update version in pyproject.toml (or setup.py)
4. Update CHANGELOG.md with version header
5. Commit with message "Release vX.Y.Z"
6. Create git tag vX.Y.Z
7. Push to origin with --tags
```

Claude follows this like a recipe.

## The Exercise

### Create a Daily Standup Skill

```
Create a skill called "standup" that:
1. Shows git commits from the last 24 hours
2. Shows current branch and any uncommitted changes
3. Lists any TODO comments added recently
4. Summarizes in a format suitable for a standup meeting
```

Now each morning:

```
/standup
```

You get a summary ready for your team.

### Create a PR Review Skill

```
Create a skill called "review-pr" that takes a PR number and:
1. Fetches the PR details
2. Shows the diff
3. Analyzes the changes for potential issues
4. Suggests improvements
```

Usage:

```
/review-pr 42
```

## When to Use Skills vs Commands

### Use Slash Commands for:
- Single command execution (`/test`, `/lint`)
- No input needed
- Quick, simple actions

### Use Skills for:
- Multi-step workflows
- Need user input
- Complex logic
- Want to encapsulate best practices

## Managing Your Automations

```
List all my custom slash commands and skills.
```

```
Delete the /release skill, I want to rewrite it.
```

```
Edit the /test command to also include coverage.
```

## Commit

Try out your new `/commit` command:

```
/commit
```

---

[Next: Chapter 9 - Hooks →](09-hooks.md)

---

## Skills Learned

- [ ] Creating slash commands
- [ ] Creating skills
- [ ] Skill file structure
- [ ] When to use skills vs commands

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 7: Make It Pretty](07-make-it-pretty.md) | [README](../README.md) | [Chapter 9: Hooks](09-hooks.md) |
