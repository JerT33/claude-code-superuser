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
| **Core Skills** | 4-7 | Planning workflow, extended thinking, visual feedback, context management |
| **Production Ready** | 8-10 | Persistence, testing, hooks, git workflows |
| **Advanced** | 11-13 | Custom automation, multi-session orchestration, CI/headless mode |
| **Reference** | 14 | Cheat sheet and anti-patterns |

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
# Open docs/00-the-broken-app.md
```

## Chapters

### Phase 0: Setup
- [Chapter 0: The Broken App](docs/00-the-broken-app.md) - See what you're working with

### Phase 1: Foundation
- [Chapter 1: Global Setup](docs/01-global-setup.md) - Configure Claude Code with planning-first principles
- [Chapter 2: Project Init](docs/02-project-init.md) - Initialize Claude Code in the project
- [Chapter 3: Quick Wins](docs/03-quick-wins.md) - Fix obvious bugs, learn basic commands

### Phase 2: Core Skills
- [Chapter 4: Your First Feature](docs/04-first-feature.md) - Add configurable timer with full planning workflow
- [Chapter 5: Make It Pretty](docs/05-make-it-pretty.md) - Use visual feedback to improve the CLI
- [Chapter 6: External Docs](docs/06-external-docs.md) - Fetch library documentation with plugins
- [Chapter 7: Context Mastery](docs/07-context-mastery.md) - Manage context like a pro

### Phase 3: Production Ready
- [Chapter 8: Persistence & Stats](docs/08-persistence-stats.md) - Add session history with scope discipline
- [Chapter 9: Testing & Hooks](docs/09-testing-hooks.md) - Add tests and automate quality checks
- [Chapter 10: Git Workflows](docs/10-git-workflows.md) - Branches, PRs, and professional git

### Phase 4: Advanced
- [Chapter 11: Custom Automation](docs/11-custom-automation.md) - Create your own skills and commands
- [Chapter 12: Multi-Session Workflows](docs/12-multi-session.md) - Orchestrate parallel work with /resume
- [Chapter 13: Advanced Config](docs/13-advanced-config.md) - Permissions, headless mode, team setup

### Reference
- [Chapter 14: Cheat Sheet & Anti-Patterns](docs/14-cheatsheet.md) - Quick reference and common mistakes

## Skills You'll Learn

By completing this tutorial, you'll master **40 Claude Code skills** across these categories:

- **Setup & Configuration** - Global/project CLAUDE.md, init, allow settings
- **Core Workflow** - Task classification, planning-first, scope discipline
- **Context Management** - Monitor, compress, clear, revert, resume
- **Thinking Modes** - `think`, `ultrathink`, model switching
- **Visual Feedback** - Screenshots, image input
- **Git Integration** - `/commit`, `/pr`, branches, stacked PRs
- **External Resources** - MCP plugins, context7, web fetch
- **Automation** - Hooks, skills, slash commands, custom agents
- **Advanced** - Multi-session, headless/CI, permissions

## Contributing

Found a bug in the tutorial (not the intentional ones!)? Want to improve an explanation? PRs welcome.

## License

MIT
