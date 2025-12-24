# lib/schemas/

Schema files used by scripts for validation, generation, and data structure definition.

## Purpose

This directory contains schema files that scripts use for:
- Validating input data
- Generating code or configuration files
- Defining expected data structures
- Documenting data formats

## Distinction from .templx/schemas/

The schemas here are different from those in `.templx/schemas/`:
- `.templx/schemas/` - System-level schemas for templx data formats (manifests, etc.)
- `lib/schemas/` - Script-level schemas used programmatically by commands

## File Formats

Common schema formats:
- JSON Schema (.json)
- YAML Schema (.yml)
- XML Schema (.xsd)

## Naming Convention

Use kebab-case for schema filenames and descriptive names that indicate what they validate or define.
