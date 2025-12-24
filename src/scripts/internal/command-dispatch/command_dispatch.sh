#!/usr/bin/env bash
# templx Command Dispatcher

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

case "$1" in
    pack)
        exec "$SCRIPT_DIR/../../commands/pack/pack" "$@"
        ;;
    unpack)
        exec "$SCRIPT_DIR/../../commands/unpack/unpack" "$@"
        ;;
    create)
        exec "$SCRIPT_DIR/../../commands/create/create" "$@"
        ;;
    validate)
        exec "$SCRIPT_DIR/../../commands/validate/validate" "$@"
        ;;
    styles-list)
        exec "$SCRIPT_DIR/../../commands/style/styles-list" "$@"
        ;;
    styles-import)
        exec "$SCRIPT_DIR/../../commands/style/styles-import" "$@"
        ;;
    styles-import-snippet)
        exec "$SCRIPT_DIR/../../commands/style/styles-import-snippet" "$@"
        ;;
    inventory)
        exec "$SCRIPT_DIR/../../commands/inventory/inventory" "$@"
        ;;
    manifest-*)
        exec "$SCRIPT_DIR/../../commands/manifest-utils/manifest" "$@"
        ;;
    help|--help|-h)
        echo "templx"
        echo ""
        echo "Usage: templx <command> [args...]"
        echo ""
        echo "Commands:"
        echo "  pack <target-file>                       - Package OpenXML document from expanded directory"
        echo "  unpack <target-file>                     - Unpack OpenXML document to expanded directory"
        echo "  create <file-type> [name]                - Create new template/document"
        echo "  validate <target-file>                   - Validate OpenXML document against schema"
        echo "  styles-list <template>                   - Extract and list styles from Word template"
        echo "  styles-import <target> <source>          - Import styles from source to target Word doc"
        echo "  styles-import-snippet <target> <snippet> - Import styles from XML snippet"
        echo "  inventory <command>                      - Generate template inventory"
        echo "  manifest-generate-<agency>               - Generate/update manifest for agency"
        echo "  manifest-generate-core                   - Generate core manifest from core/"
        echo "  manifest-generate-partials-builds        - Generate builds/manifests/partials-manifest.json"
        echo "  manifest-generate-partials-core          - Generate core/partials/partials-manifest.json"
        echo "  manifest-validate                        - Validate all manifests"
        echo "  manifest-list                            - List all templates"
        echo "  manifest-update-status                   - Update template status (manifest-update-status <agency> <template> <status>)"
        echo "  manifest-add-template                    - Display guide for adding template (manifest-add-template <agency> <template> <type>)"
        echo "  help                                     - Show this help message"
        echo ""
        echo "Run '<command> help' for command-specific options"
        ;;
    *)
        echo "Unknown command: $1"
        echo "Run 'templx help' for usage information"
        exit 1
        ;;
esac