# Chapter 10: Git Workflows

You've been committing to main. Time to level up with branches, PRs, and professional git workflows.

## Branch-Based Development

Real projects use feature branches:
1. Create branch for feature
2. Work on branch
3. Create PR
4. Merge after review

Let's practice this with Claude Code.

## The Exercise

### Step 1: Create a Feature Branch

```
Create a new branch called "feature/break-timer" for adding
break timers between pomodoros.
```

Claude will:
```bash
git checkout -b feature/break-timer
```

### Step 2: Implement on the Branch

```
Add a break timer feature:
- After a pomodoro ends, offer a 5-minute break
- Make the break duration configurable
- Show a different message/color during break
```

Work through the implementation. Commit as you go:

```
/commit
```

### Step 3: Create a Pull Request

```
/pr
```

Claude will:
1. Push the branch to origin
2. Create a PR using `gh pr create`
3. Generate a description based on commits

<!-- SCREENSHOT: Claude creating a PR with /pr -->

The PR will include:
- Summary of changes
- Test plan (if applicable)
- Link to any issues

### Step 4: View the PR

Claude will output the PR URL. Open it in your browser to see the formatted description.

## Stacked PRs

For larger features, you might want multiple PRs that build on each other. This is called "stacked PRs."

### Example Stack

```
main
  └── feature/break-timer (PR #1)
        └── feature/break-timer-sound (PR #2)
              └── feature/break-timer-skip (PR #3)
```

Each PR is small and reviewable. They merge in order.

### Creating a Stack

```
We're on feature/break-timer. Create a new branch from here
called feature/break-timer-sound to add sound alerts for breaks.
```

Claude creates the branch building on your current work:

```bash
git checkout -b feature/break-timer-sound
```

Implement and commit:

```
Add a sound alert when the break starts and ends.
```

```
/commit
```

Create PR targeting the previous branch:

```
Create a PR for this branch targeting feature/break-timer (not main).
```

## Working Across Branches

### Switching Context

When you switch branches, Claude's context persists but the files change:

```
Switch to the main branch
```

```bash
git checkout main
```

Now if you ask Claude about the break timer code, it won't be there (it's on the feature branch).

### Managing Multiple Features

You might be working on multiple features:

```
git checkout -b feature/daily-goals
```

Work on this, then switch back:

```
git checkout feature/break-timer
```

Claude Code handles this naturally—it reads files as needed.

## PR Workflow Commands

| Command | What It Does |
|---------|--------------|
| `/pr` | Create a new PR for current branch |
| `gh pr view` | View current PR details |
| `gh pr checks` | See CI check status |
| `gh pr merge` | Merge the PR |

## Commit Messages

Claude generates commit messages based on the changes. Good ones look like:

```
Add configurable break timer between pomodoros

- Break duration defaults to 5 minutes
- Can be set with --break-minutes flag
- Shows blue progress bar during break
```

If you don't like the message Claude generates:

```
Rewrite that commit message to be more specific about [aspect].
```

## Cleanup

After PRs merge:

```
Switch to main, pull latest, and delete the merged feature branches.
```

```bash
git checkout main
git pull
git branch -d feature/break-timer
```

---

[Next: Chapter 11 - Custom Automation →](11-custom-automation.md)

---

## Skills Learned

- [ ] Feature branch workflow
- [ ] `/pr` command
- [ ] Working across multiple branches
- [ ] Stacked PRs concept
- [ ] Branch context management

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 9: Testing & Hooks](09-testing-hooks.md) | [README](../README.md) | [Chapter 11: Custom Automation](11-custom-automation.md) |
