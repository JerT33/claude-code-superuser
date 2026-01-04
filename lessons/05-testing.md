# Chapter 5: Testing

The off-by-one bug from Chapter 0? A simple unit test would have caught it. Let's add tests to make sure bugs can't sneak back in.

## The Exercise

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

## When to Add Tests

A good rule of thumb:
- **Bug fixes** - Add a test that would have caught the bug
- **New features** - Add tests for the happy path and edge cases
- **Refactoring** - Ensure existing tests pass before and after

You don't need 100% coverage. Focus on testing logic that matters.

## Commit

Once tests are passing:

```
commit these changes
```

---

[Next: Chapter 6 - Context Mastery →](06-context-mastery.md)

---

## Skills Learned

- [ ] Adding tests with Claude
- [ ] Running tests
- [ ] Test-driven bug fixing
- [ ] When to add tests

## Navigation

| Previous | Up | Next |
|----------|-----|------|
| [Chapter 4: First Feature](04-first-feature.md) | [README](../README.md) | [Chapter 6: Context Mastery](06-context-mastery.md) |
