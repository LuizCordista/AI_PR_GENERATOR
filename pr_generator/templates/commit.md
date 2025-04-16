# Conventional Commit Message Generator

This script analyzes a git diff and generates an appropriate conventional commit message.

## Input

Paste the git diff below:

{{diff}}

## Instructions

1. Analyze the provided diff.
2. Determine the type of change (feat, fix, docs, style, refactor, perf, test, chore).
3. Identify the scope of the change, if applicable.
4. Create a short and meaningful description of the change.
5. If necessary, add a more detailed body to the commit message.
6. If there are breaking changes, add a footer with the details.

## Output

Based on the diff analysis, here is the suggested conventional commit message:

<type>(<scope>): <description>

[optional body]

[optional footer(s)]


### Explanation

- **Type**: The type of change (feat, fix, docs, etc.)
- **Scope**: The part of the code affected (optional)
- **Description**: Brief description of the change
- **Body**: Additional details, if necessary
- **Footer**: Information about breaking changes, if any

## Additional Notes

- The subject line (first line) should not exceed 50 characters
- The body should be wrapped at 72 characters
- Use present tense ("add feature" not "added feature")
- The body should explain the "what" and "why", not the "how"

Always return in English