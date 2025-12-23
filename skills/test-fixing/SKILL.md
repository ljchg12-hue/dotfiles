---
name: test-fixing
description: Automatically diagnose and fix failing tests by analyzing errors, updating assertions, and refactoring test code
---

# Test Fixing Skill

Diagnose and fix failing tests automatically using error analysis and intelligent refactoring.

## When to Use
- Failing test suite
- Flaky tests
- Test maintenance
- CI/CD pipeline failures

## Core Capabilities
- Error analysis and root cause identification
- Assertion updates
- Mock/stub fixing
- Timeout adjustments
- Race condition detection
- Test data refresh
- Dependency updates

## Common Fixes
```javascript
// Fix 1: Update assertion
- expect(result).toBe(5);
+ expect(result).toBe(6); // Updated expected value

// Fix 2: Add async/await
- it('should fetch data', () => {
-   const data = fetchData();
+ it('should fetch data', async () => {
+   const data = await fetchData();

// Fix 3: Fix mock
- jest.mock('./api');
+ jest.mock('./api', () => ({
+   fetchUser: jest.fn().mockResolvedValue({ id: 1 })
+ }));

// Fix 4: Increase timeout
- it('slow test', () => {
+ it('slow test', () => {
+   jest.setTimeout(10000);
```

## Best Practices
- Analyze error messages first
- Check for environmental issues
- Update test data regularly
- Fix flaky tests immediately
- Run tests in isolation

## Resources
- Jest: https://jestjs.io/
- Testing Library: https://testing-library.com/
