# Chapter 5: Git Workflows

You've been committing to main. Time to level up with branches and PRs.

## The Exercise

### Step 1: Create a Feature Branch

```
Create a new branch called "feature/break-timer" for adding
break timers between pomodoros.
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
commit these changes
```

### Step 3: Create a Pull Request

```
create a pull request
```

Claude will:
1. Push the branch to origin
2. Create a PR using `gh pr create`
3. Generate a description based on commits

### Step 4: View the PR

Claude will output the PR URL. Open it in your browser to see the formatted description.

## PR Commands

| Command | What It Does |
|---------|--------------|
| `create a pull request` | Create PR for current branch |
| `gh pr view` | View current PR details |
| `gh pr checks` | See CI check status |
| `gh pr merge` | Merge the PR |

---

[Next: Chapter 6 - Testing →](06-testing.md)

---

## Skills Learned

- [ ] Feature branch workflow
- [ ] Creating pull requests
- [ ] PR commands

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 4: First Feature](04-first-feature.md) | [README](../README.md) | [Chapter 6: Testing](06-testing.md) |
