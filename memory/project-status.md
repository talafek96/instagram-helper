---
name: project-status
type: project
description: Live snapshot of the Instagram helper
---
Snapshot 2026-11-19
- Done: both accounts connected, DMs readable, profile/insights work, account switching
  (`list_accounts` / `use_account`). Registered as user-scope MCP `instagram`.
  `instagram-expert` subagent available in every project (symlink in ~/.claude/agents).
- Untested: publishing, comments, insights tools under Unified login (upstream wrote them for
  graph.instagram.com; most should work via the `me`→id mapping, verify before relying on them).
- Next: nothing pending. If Tal makes @talafek96 private again, re-check DM access.

## Backlog (Tal: "stay with this now", 2026-11-19)
- **Media tools:** `download_media` (photos/videos/voice notes via the attachment URLs, saved under a
  gitignored `data/private/`) + `transcribe_audio` like whatsapp-helper. Untested which attachment
  fields come back on our chats (scan hit the rate limit): test on ONE chat first.
- **Full history, past:** import Instagram's "Export your information" (Messages, JSON; includes
  media) into a local searchable store. Official, no ban risk.
- **Full history, future:** webhooks → small Cloudflare Worker that archives every new message, so
  nothing falls out of the 20-message window.
- **Deep dives meanwhile:** scroll instagram.com/direct in Tal's Chrome (Claude in Chrome).
- **Unofficial MCP (not recommended):** trypeggy/instagram_dm_mcp (instagrapi; full history + media
  download, no voice notes). Password login, ToS violation, ban risk; unmaintained since 2025-08.
  If ever tried: @talafek96 only, session-cookie login, never the business account.
