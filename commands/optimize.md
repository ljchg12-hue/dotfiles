Analyze and optimize performance bottlenecks.

## What this command does
Invokes the `perf-analyst` agent to identify and fix performance issues.

## Analysis includes
- Database query optimization
- API response times
- Frontend rendering performance
- Memory usage patterns
- Algorithm complexity

## Usage
```
/project:optimize                # Analyze entire project
/project:optimize src/api/       # Focus on API routes
/project:optimize --db           # Focus on database queries
/project:optimize file.ts        # Analyze specific file
```

## Instructions for the agent

1. Establish baseline metrics:
   - API response times
   - Database query times
   - Memory usage
   - Bundle sizes (frontend)

2. Identify common issues:
   - N+1 queries
   - Missing database indexes
   - Unnecessary re-renders
   - Memory leaks
   - Large payloads
   - Blocking operations

3. For database optimization:
   ```sql
   EXPLAIN ANALYZE SELECT ...
   ```
   - Add missing indexes
   - Optimize slow queries
   - Implement caching

4. For frontend optimization:
   - Code splitting
   - Lazy loading
   - Memoization
   - Virtual lists

5. Provide output in this format:
   ```
   ## Performance Analysis Report

   ### Baseline Metrics
   - API Response: Xms (p50), Yms (p95)
   - DB Queries: Xms average
   - Memory: X MB peak

   ### Identified Bottlenecks
   1. [Issue with evidence]
      - Location: file:line
      - Impact: [description]

   ### Optimizations Applied
   1. [What was optimized]
      - Before: X
      - After: Y
      - Improvement: Z%

   ### Recommendations
   1. [Additional optimizations to consider]
   ```
