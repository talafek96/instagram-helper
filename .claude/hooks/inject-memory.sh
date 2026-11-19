#!/usr/bin/env bash
# SessionStart (incl. after compaction): inject the index, status and feedback rules.
set -euo pipefail
MEM="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)/memory"
[ -d "$MEM" ] || exit 0
strip() { awk 'BEGIN{fm=0} /^---$/{fm++; next} fm>=2 || fm==0' "$1"; }
echo "<instagram-helper-memory>"
cat "$MEM/MEMORY.md"; echo
[ -f "$MEM/project-status.md" ] && { echo "## Status"; strip "$MEM/project-status.md"; echo; }
echo "## Standing rules (full text)"
for f in "$MEM"/feedback-*.md; do [ -f "$f" ] && { echo; echo "### $(basename "$f" .md)"; strip "$f"; }; done
echo "</instagram-helper-memory>"
