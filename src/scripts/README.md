# Scripts Directory

This directory contains all the command-line tools and utilities for templx.

## Structure

```
scripts/
├── bin/              # User-facing command entry points (add to PATH)
├── commands/         # Command implementations
├── lib/              # Shared libraries and utilities
└── internal/         # Internal scripts (not user-facing)
```

## Directory Purpose

### `bin/`
Contains executable wrapper scripts that users call directly. These are thin wrappers that dispatch to the actual implementations in `commands/`. Add this directory to your PATH.

### `commands/`
Contains the actual command implementations. Each command may be:
- A single executable file (for simple commands)
- A directory with multiple files (for complex commands)

All directories use kebab-case naming.

### `lib/`
Shared bash libraries and utilities that can be sourced by multiple commands. This promotes DRY (Don't Repeat Yourself) principles.

### `internal/`
Scripts used internally by the system but not meant to be called directly by users:
- `command-dispatch/` - Central command dispatcher
- `setup-aliases/` - Shell setup scripts

## Adding New Commands

1. Create implementation in `commands/`
2. Add wrapper script in `bin/`
3. Update `command-dispatch.sh` if needed
4. Document in command's README (if complex)

## Naming Conventions

- **Directories**: kebab-case (e.g., `manifest-utils`)
- **Scripts**: kebab-case (e.g., `style-import`)
- **Functions**: snake_case (e.g., `generate_manifest`)
