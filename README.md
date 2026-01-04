# Claude Code Superuser

An interactive tutorial to master Claude Code by fixing and enhancing a broken Pomodoro timer app.

## What Is This?

This repo contains a deliberately broken Python app and a series of hands-on chapters that teach you Claude Code skills by having you fix and improve it. By the end, you'll have transformed a buggy mess into a polished, tested, feature-rich CLI tool—and you'll be a Claude Code power user.

**This is not documentation.** This is learning by doing.

## Who Is This For?

Experienced engineers who want to:
- Get productive with Claude Code quickly
- Learn advanced features (multi-session workflows, custom agents, hooks)
- Develop best practices for AI-assisted development

## The Journey

| Phase | Chapters | What You'll Learn |
|-------|----------|-------------------|
| **Foundation** | 0-3 | Setup, project init, basic commands, first commits |
| **Core Skills** | 4-7 | Plan mode, git workflows, testing, context management |
| **Power Features** | 8-10 | Visual feedback, custom automation, hooks |
| **Advanced** | 11-12 | Permissions, headless/CI, multi-session orchestration |
| **Reference** | 13 | Cheat sheet and anti-patterns |

## The App's Transformation

```
BEFORE                              AFTER
──────                              ─────
- Typos everywhere                  - Clean, professional output
- Timer shows wrong time            - Accurate countdown
- Crashes on pause                  - Robust error handling
- Hardcoded 25 minutes              - Configurable durations
- Ugly plain text                   - Beautiful CLI with colors
- No persistence                    - Session history & stats
- No tests                          - Full test suite
- No automation                     - Custom skills & hooks
```

## Getting Started

### Prerequisites

- [Claude Code](https://claude.ai/code) installed and configured
- Python 3.8+
- Git

### Quick Start

```bash
# Fork this repo, then clone your fork
git clone https://github.com/YOUR_USERNAME/claude-code-superuser.git
cd claude-code-superuser

# See the broken app in action
python src/pomodoro.py start

# Start the tutorial
# Open lessons/00-the-broken-app.md
```

## Chapters

### Phase 1: Foundation
- [Chapter 0: The Broken App](lessons/00-the-broken-app.md) - See what you're working with
- [Chapter 1: Global Setup](lessons/01-global-setup.md) - Configure Claude Code with planning-first principles
- [Chapter 2: Project Init](lessons/02-project-init.md) - Initialize Claude Code in the project
- [Chapter 3: Quick Wins](lessons/03-quick-wins.md) - Fix obvious bugs, learn basic commands

### Phase 2: Core Skills
- [Chapter 4: First Feature](lessons/04-first-feature.md) - Plan mode, extended thinking, scope discipline
- [Chapter 5: Git Workflows](lessons/05-git-workflows.md) - Branches, PRs, and professional git
- [Chapter 6: Testing](lessons/06-testing.md) - Add tests with pytest
- [Chapter 7: Context Mastery](lessons/07-context-mastery.md) - Manage context like a pro

### Phase 3: Power Features
- [Chapter 8: Make It Pretty](lessons/08-make-it-pretty.md) - Use visual feedback to improve the CLI
- [Chapter 9: Custom Automation](lessons/09-custom-automation.md) - Create your own slash commands and skills
- [Chapter 10: Hooks](lessons/10-hooks.md) - Automate quality checks

### Phase 4: Advanced
- [Chapter 11: Advanced Config](lessons/11-advanced-config.md) - Permissions, headless mode, team setup
- [Chapter 12: Multi-Session Workflows](lessons/12-multi-session.md) - Orchestrate parallel work with /resume

### Reference
- [Chapter 13: Cheat Sheet & Anti-Patterns](lessons/13-cheatsheet.md) - Quick reference and common mistakes

## Skills You'll Learn

By completing this tutorial, you'll master Claude Code skills across these categories:

- **Setup & Configuration** - Global/project CLAUDE.md, init, allow settings
- **Core Workflow** - Task classification, planning-first, scope discipline
- **Context Management** - Monitor, compress, clear, revert, resume
- **Thinking Modes** - `think`, `ultrathink`
- **Visual Feedback** - Screenshots, image input
- **Git Integration** - Commits, branches, PRs, stacked PRs
- **Automation** - Hooks, custom slash commands, skills
- **Advanced** - Multi-session, headless/CI, permissions

## Contributing

Found a bug in the tutorial (not the intentional ones!)? Want to improve an explanation? PRs welcome.

## License

MIT
