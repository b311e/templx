# internal/

Internal scripts not meant to be called directly by users.

## Purpose

This directory contains scripts that:
- Support the command infrastructure
- Are called by other scripts
- Should not be in user's PATH
- Provide system-level functionality

## Contents

### `command-dispatch/`
Central command dispatcher that routes `templx <command>` calls to the appropriate implementation in `commands/`.

### `setup-aliases/`
Shell setup scripts for bash/zsh/PowerShell that configure PATH and aliases.

## What Goes Here

- Infrastructure scripts
- Setup/configuration tools
- Internal utilities
- Meta-scripts that manage other scripts

## What Doesn't Go Here

- User-facing commands (goes in `bin/`)
- Command implementations (goes in `commands/`)
- Shared utilities (goes in `lib/`)

## Naming Convention

Use kebab-case for all directory and file names to maintain consistency with the rest of the project.
