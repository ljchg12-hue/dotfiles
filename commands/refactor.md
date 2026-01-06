Refactor code to improve structure and maintainability.

## What this command does
Invokes the `refactor-expert` agent to improve code quality without changing behavior.

## Refactoring includes
- Apply SOLID principles
- Reduce code complexity
- Extract reusable functions
- Apply design patterns
- Remove code smells

## Usage
```
/project:refactor                # Suggest refactorings
/project:refactor src/utils/     # Refactor specific directory
/project:refactor file.ts        # Refactor specific file
/project:refactor --complexity   # Focus on reducing complexity
```

## Instructions for the agent

1. **Before refactoring**:
   - Ensure tests exist and pass
   - Understand the current behavior
   - Identify code smells

2. **Code smells to address**:
   - Long functions (>20 lines)
   - Large classes (>300 lines)
   - Duplicate code
   - Long parameter lists
   - Feature envy
   - Primitive obsession
   - Switch statements (consider polymorphism)

3. **Refactoring techniques**:
   - Extract Method
   - Extract Class
   - Replace Conditional with Polymorphism
   - Introduce Parameter Object
   - Move Method
   - Inline Method (if too fragmented)

4. **Safe refactoring process**:
   - Make one change at a time
   - Run tests after each change
   - Commit frequently

5. **Provide output in this format**:
   ```
   ## Refactoring Report

   ### Code Smells Identified
   1. [Smell] in file:line
      - Issue: [description]
      - Suggested refactoring: [technique]

   ### Refactorings Applied
   1. [What was changed]
      - Before: [code snippet]
      - After: [code snippet]
      - Reason: [why this improves the code]

   ### Metrics
   - Cyclomatic complexity: X → Y
   - Lines of code: X → Y
   - Duplicated code: X% → Y%

   ### Tests
   - All tests passing: ✅
   ```
