# Manifest Utilities

This folder contains scripts for managing templates and manifests in templx.

## manifest

Unified script for all manifest operations: generate agency manifests, update template status, validate, list templates, and update core manifests.

Usage:

Note: ensure `src/scripts/bin` is on your PATH (see top-level README). You can run the hyphenated wrappers in `src/scripts/bin` (e.g. `manifest-generate-partials-builds`) or use the unified `manifest <action> <resource>` form.


- `manifest-generate <agency>` or `manifest-generate-agency <agency>` - Generate/update manifest timestamp and scan for templates for an agency.
- `manifest-update-status <agency> <template> <status>` - Update template status in an agency manifest.
- `manifest-add-template <agency> <template> <type>` - Display guide for adding a new template to an agency.
- `manifest-validate` - Validate all manifests.
- `manifest-list` - List all templates across `builds/`.
- `manifest-generate-core` or `manifest-generate core` - Generate `core/manifests/manifest.json` from components in `core/`.
- `manifest-generate-partials-builds` - Generate partials manifest by scanning `builds/*/partials` and writing `builds/manifests/partials-manifest.json`.
- `manifest-generate-partials-core` - Generate partials manifest by scanning `core/partials` and writing `core/partials/partials-manifest.json`.
- `manifest-generate-partials-core` - Generate partials manifest by scanning `core/partials` and writing `core/manifests/partials-manifest.json`.