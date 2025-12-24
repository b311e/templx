# commands/

Command implementations for templx.

## Structure

This directory contains all command implementations, organized by functionality:

- **cleanup-wordml/** - Clean up Word document markup
- **create/** - Create new templates/documents
- **inventory/** - Generate template inventories
- **manifest-utils/** - Manifest generation and management
- **pack/** - Package OpenXML files
- **style/** - Style import/export utilities
- **unpack/** - Unpack OpenXML files
- **validate/** - Validate OpenXML documents
- **xpathsel/** - XPath selector utility

## Naming Conventions

- Use **kebab-case** for all directory names
- Use **kebab-case** for all script names
- Match the user-facing command name

## Directory vs Single File

**Use a directory when:**
- Multiple related files needed
- Complex logic requiring helpers
- Tests should be co-located
- Documentation needed

**Use a single file when:**
- Self-contained < 100 lines
- No dependencies or helpers
- Logic is straightforward

## Adding a New Command

1. Create directory or file: `commands/my-command/`
2. Add executable script: `commands/my-command/my-command`
3. Add README.md if complex
4. Create wrapper in `../bin/my-command`
5. Update `../internal/command-dispatch/command_dispatch.sh` if needed

## Command Requirements

Each command should:
- Have a `--help` flag
- Return proper exit codes (0 = success, non-zero = error)
- Print errors to stderr, output to stdout
- Follow the wrapper pattern used in `bin/`
