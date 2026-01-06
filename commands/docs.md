Generate or update documentation for the project.

## What this command does
Invokes the `doc-writer` agent to create or update project documentation.

## Documentation types
- README.md with setup instructions
- API documentation (OpenAPI 3.0)
- Code comments (JSDoc/TSDoc)
- CHANGELOG updates
- User guides

## Usage
```
/project:docs                    # Update README.md
/project:docs readme             # Generate/update README
/project:docs api                # Generate API documentation
/project:docs changelog          # Update CHANGELOG.md
/project:docs jsdoc src/         # Add JSDoc comments
```

## Instructions for the agent

1. Analyze the project structure to understand:
   - Tech stack used
   - Main features
   - Dependencies
   - Configuration requirements

2. For README.md:
   - Project description
   - Features list
   - Installation steps
   - Environment variables
   - Usage examples
   - API reference link

3. For API documentation:
   - Generate OpenAPI 3.0 spec
   - Document all endpoints
   - Include request/response examples
   - Document authentication

4. For CHANGELOG:
   - Follow Keep a Changelog format
   - Group by: Added, Changed, Fixed, Deprecated, Removed
   - Include version and date

5. For JSDoc/TSDoc:
   - Add comments to exported functions
   - Include @param, @returns, @example
   - Document complex types

6. Writing principles:
   - Clear and concise
   - Include examples
   - No jargon without explanation
   - Keep updated with code changes
