# bin/

User-facing command entry points for templx.

## What Goes Here

This directory contains **only** thin wrapper scripts that:
1. Are added to the user's PATH
2. Dispatch to implementations in `../commands/`
3. Require minimal logic (just path resolution and exec)

## What Doesn't Go Here

- Complex logic (goes in `commands/`)
- Shared utilities (goes in `lib/`)
- Internal scripts (goes in `internal/`)

## Wrapper Pattern

All wrappers follow this pattern:

```bash
#!/usr/bin/env bash
exec "$(dirname "$0")/../commands/COMMAND/COMMAND" "$@"
```

Or for commands needing dynamic path resolution:

```bash
#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "$SCRIPT_DIR/../commands/COMMAND/COMMAND" "$@"
```

## Adding a New Wrapper

1. Create file with command name (no extension)
2. Make executable: `chmod +x filename`
3. Follow wrapper pattern above
4. Point to correct path in `commands/`
