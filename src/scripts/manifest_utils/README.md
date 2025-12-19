# Manifest Utilities

This folder contains scripts for managing templates and manifests in the COGA Template Manager.

## manifest

Unified script for all manifest operations: generate agency manifests, update template status, validate, list templates, and update core manifests.

Usage:

- `manifest-generate <agency>` or `manifest-generate-agency <agency>` - Generate/update manifest timestamp and scan for templates for an agency.
- `manifest-update-status <agency> <template> <status>` - Update template status in an agency manifest.
- `manifest-add-template <agency> <template> <type>` - Display guide for adding a new template to an agency.
- `manifest-validate` - Validate all manifests.
- `manifest-list` - List all templates across `builds/`.
- `manifest-generate-core` or `manifest-generate core` - Generate `core/manifest.json` from components in `core/`.
- `manifest-generate-partials [core]` - Generate partials manifest; omit scope to scan `builds/*/partials`, pass `core` to scan `core/partials`.