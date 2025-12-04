# Manifest Utilities

This folder contains scripts for managing templates and manifests in the COGA Template Manager.

## manifest

Unified script for all manifest operations: generate agency manifests, update template status, validate, list templates, and update core manifests.

Usage:

- `manifest-generate <agency>` - Generate/update manifest timestamp and scan for templates.
- `manifest-update-status <agency> <template> <status>` - Update template status.
- `manifest-add-template <agency> <template> <type>` - Display guide for adding new template.
- `manifest-validate` - Validate all manifests.
- `manifest-list` - List all templates.
- `manifest-generate core` - Generate core/manifest.json from components in core/.