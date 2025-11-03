#!/bin/bash
set -euo pipefail

WORK_DIR="$(pwd)"

# Replace secrets in configuration files
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
./replace_secrets.py

# Hand off to the default entrypoint
cd "$WORK_DIR"
exec /init "$@"