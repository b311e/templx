# lib/templates/

Template files used for generating code-related files (snippets, scripts, etc.).

## Purpose

This directory contains template files that serve as scaffolds for creating:
- Snippet files
- Configuration files
- Script boilerplate
- Other code-related artifacts

## Distinction from Document Templates

These templates are different from the document templates (.dotm, .xltx) stored in `builds/`. Those are the actual Word/Excel templates that this system manages. The templates in this directory are used to generate supporting files for the templx system itself.

## Usage

When creating new files programmatically (e.g., generating snippet files), commands should reference templates from this directory.

## Naming Convention

- Use kebab-case for template filenames
- Use descriptive names that indicate what the template generates
- Consider using file extensions that match what they generate (e.g., `snippet.xml.template`)
