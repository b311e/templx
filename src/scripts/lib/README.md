# lib/

Shared libraries and utilities for templx scripts.

## Purpose

This directory contains reusable bash functions and utilities that can be sourced by multiple commands.

## What Goes Here

- Common bash functions used by 2+ commands
- Shared validation logic
- Path manipulation utilities
- Error handling helpers
- Logging utilities

## What Doesn't Go Here

- Command-specific logic (goes in `commands/`)
- User-facing scripts (goes in `bin/`)
- One-off utilities used by single command

## Usage Pattern

```bash
#!/usr/bin/env bash

# Source library
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../../lib/common.sh"

# Use functions
validate_file "$input_file"
log_info "Processing complete"
```

## Planned Libraries

Future libraries to add:
- `common.sh` - Common bash utilities
- `openxml.sh` - OpenXML-specific functions
- `validation.sh` - Input validation helpers
- `logging.sh` - Structured logging

## Creating a New Library

1. Create file: `lib/my-library.sh`
2. Add header comment explaining purpose
3. Define functions with clear names
4. Document each function with comments
5. Test in isolation before using
