#!/usr/bin/env bash
# COGA Template Manager Command Dispatcher

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

case "$1" in
    pack)
        exec "$SCRIPT_DIR/../pack/pack" "$@"
        ;;
    unpack)
        exec "$SCRIPT_DIR/../unpack/unpack" "$@"
        ;;
    create)
        exec "$SCRIPT_DIR/../create/create" "$@"
        ;;
    validate)
        exec "$SCRIPT_DIR/../validate/validate" "$@"
        ;;
    styles-list)
        exec "$SCRIPT_DIR/../styles/styles-list" "$@"
        ;;
    styles-import)
        exec "$SCRIPT_DIR/../styles_import/styles-import" "$@"
        ;;
    styles-import-snippet)
        exec "$SCRIPT_DIR/../styles_import/styles-import-snippet" "$@"
        ;;
    inventory)
        exec "$SCRIPT_DIR/../inventory/inventory" "$@"
        ;;
    manifest-*)
        exec "$SCRIPT_DIR/../manifest_utils/manifest" "$@"
        ;;
    help|--help|-h)
        echo "COGA Template Manager"
        echo ""
        echo "Usage: coga <command> [args...]"
        echo ""
        echo "Commands:"
        echo "  pack <dir>                      - Package OpenXML document from expanded directory"
        echo "  unpack <file>                   - Unpack OpenXML document to expanded directory"
        echo "  create <type> [name]            - Create new template/document"
        echo "  validate <file>                 - Validate OpenXML document against schema"
        echo "  styles-list <template>          - Extract and list styles from Word template"
        echo "  styles-import <target> <source> - Import styles from source to target Word doc"
        echo "  styles-import-snippet <target> <snippet> - Import styles from XML snippet"
        echo "  inventory <command>             - Generate template inventory"
        echo "  manifest generate <agency>      - Generate/update manifest for agency (use 'manifest generate agency <name>')"
        echo "  manifest generate core          - Generate core manifest from core/"
        echo "  manifest generate partials      - Generate builds/manifests/partials-manifest.json"
        echo "  manifest validate               - Validate all manifests"
        echo "  manifest list                   - List all templates"
        echo "  manifest update status          - Update template status (manifest update status <agency> <template> <status>)"
        echo "  manifest add template           - Display guide for adding template (manifest add template <agency> <template> <type>)"
        echo "  help                            - Show this help message"
        echo ""
        echo "Run '<command> help' for command-specific options"
        ;;
    *)
        echo "Unknown command: $1"
        echo "Run 'coga help' for usage information"
        exit 1
        ;;
esac