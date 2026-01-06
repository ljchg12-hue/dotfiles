Run tests and automatically fix any failures.

## What this command does
Invokes the `test-runner` agent to execute tests and fix failures while preserving test intent.

## Workflow
1. Detect testing framework (Jest, Vitest, Pytest, etc.)
2. Run relevant tests
3. Analyze any failures
4. Automatically fix test issues
5. Report results with coverage

## Usage
```
/project:test                    # Run all tests
/project:test user               # Run tests matching "user"
/project:test src/auth/          # Run tests in specific directory
```

## Instructions for the agent

1. Detect the testing framework:
   ```bash
   # Check package.json for jest, vitest, mocha, etc.
   # Check for pytest.ini, pyproject.toml
   ```

2. Run the appropriate test command:
   - Jest: `npm test -- [pattern]`
   - Vitest: `npx vitest run [pattern]`
   - Pytest: `pytest [path]`

3. If tests fail:
   - Analyze the error message
   - Determine if it's a test bug or code bug
   - Fix test bugs while preserving original test intent
   - Report code bugs for manual fixing

4. Provide output in this format:
   ```
   ## Test Results

   **Total**: X tests
   **Passed**: ✅ Y
   **Failed**: ❌ Z
   **Skipped**: ⏭️ W

   ### Failed Tests (if any)
   1. `test_name`
      - File: path/to/test.ts:42
      - Error: [description]
      - Fix: [what was done]

   ### Coverage Summary
   - Statements: X%
   - Branches: Y%
   - Functions: Z%
   ```
