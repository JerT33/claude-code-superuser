---
description: Gracefully wrap up the session with summary, prompt evaluation, and learning capture
allowed-tools: Read, Write, Edit, Bash, AskUserQuestion
---

# Session Wrap-Up

Perform a complete session wrap-up by executing these steps in order:

## Step 1: Session Summary

Analyze this conversation and create a summary:
- **Accomplishments**: What was completed this session (bullet list)
- **Key Decisions**: Important choices or directions taken
- **Context**: Any important background established

## Step 2: Prompt Evaluation

Follow the evaluation instructions in @~/.claude/commands/evaluate-prompts.md

## Step 3: Unfinished Items

List any:
- Incomplete todos from the session
- Work started but not finished
- Questions raised but not resolved
- Follow-ups needed

## Step 4: Save Session Log

Generate a timestamp and a 2-3 word summary of the session topic.

Filename format: `YYYY-MM-DD-HHMMSS-summary-words.md`
Examples:
- `2025-12-29-103045-styra-policies.md`
- `2025-12-29-143022-auth-refactor.md`

Write all of the above (Steps 1-3) to:
`~/.claude/sessions/[filename]`

Format the file cleanly with headers and the session date at the top.

## Step 5: Propose Learnings

Based on this session, identify 1-5 potential learnings to remember for future sessions. These could be:
- User preferences discovered (coding style, tools, patterns)
- Project-specific knowledge (architecture, conventions, tech stack)
- Workflow preferences (how user likes to work)
- Common patterns in their requests

IMPORTANT: Keep each learning to ONE short sentence (under 15 words). Be concise to avoid bloat.

Good: "Prefers Rego for K8s admission policies"
Bad: "The user has indicated a preference for using Rego language when writing Kubernetes admission control policies for Styra"

## Step 6: Ask for Approval

Present the proposed learnings to the user and ask which ones (if any) they want to save. Use the AskUserQuestion tool with checkboxes for each learning.

## Step 7: Save Approved Learnings

For any approved learnings, append them to `~/.claude/rules/learnings.md` with today's date.

Format:
```
## [Date]
- Learning 1
- Learning 2
```

## Step 8: Final Message

Confirm what was saved:
- Session log file path
- Number of learnings added (if any)

Then display:
```
Session wrapped up. Type /exit or Ctrl+C to end.
```
