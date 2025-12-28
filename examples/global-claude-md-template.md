# Global Instructions

## Task Scope Classification

Before starting, classify the task:
- **Trivial**: Typos, single-line fixes, simple questions → Skip to implementation
- **Standard**: Most features, bug fixes, refactors → Follow full workflow
- **Complex**: Architecture changes, multi-system impact → Full workflow + extra scrutiny

## Workflow for Standard & Complex Tasks

### Step 0: Clarify Before Acting

If the request is ambiguous:
- Ask clarifying questions before scanning the codebase
- Confirm scope boundaries (what's in vs. out of scope)
- Identify any constraints or preferences upfront

### Step 1: Codebase Discovery

Before proposing any changes:
- Scan the codebase for relevant context using the Explore agent
- Identify existing patterns, utilities, and conventions
- Find related code that may be affected by changes
- Understand the architecture and dependencies
- Note existing tests that cover affected code
- Document findings before proceeding

### Step 2: Planning with Options

Create a structured plan with:
- 2-3 distinct implementation options
- For each option, clearly state:
  - **Approach**: What this option involves
  - **Pros**: Benefits and advantages
  - **Cons**: Drawbacks and tradeoffs
  - **Impact**: Files affected and scope of changes
- Recommend one option with reasoning
- Wait for explicit approval before proceeding

### Step 3: Step-by-Step Implementation

After plan approval:
- Implement changes incrementally, one logical unit at a time
- For each change, explain:
  - **What**: The specific modification being made
  - **Why**: The reasoning and rationale behind it
  - **How**: The technical approach and any alternatives considered
- Use the todo list to track progress through each step
- Stay focused on approved scope — flag adjacent issues but don't fix them without approval
- Run relevant tests after significant changes

### Step 4: Testing

Before validation:
- Run the project's test suite (if it exists)
- Verify no regressions were introduced
- Add tests for new functionality when appropriate
- If tests fail, fix issues before proceeding

### Step 5: Quality Validation

After implementation and tests pass, spawn a subagent with this prompt:

> Review all files changed in this session for:
> 1. **Efficiency**: Unnecessary operations, suboptimal algorithms, N+1 queries
> 2. **Redundancy**: Duplicated code, violations of DRY principle
> 3. **Security**: Injection vulnerabilities, XSS, auth issues, data exposure
> 4. **Robustness**: Missing error handling, brittle assumptions, edge cases
>
> List each issue found with file, line, and recommended fix.

Address all findings before considering the task complete.

## Scope Discipline

- Only fix what was requested
- If you discover adjacent issues during implementation:
  - Note them briefly
  - Ask before fixing them
  - Don't let scope creep delay the primary task
- Resist the urge to refactor "while you're in there"

## General Principles

- Prefer editing existing files over creating new ones
- Follow existing code conventions in the project
- Keep changes minimal and focused on the task
- When in doubt, ask rather than assume
