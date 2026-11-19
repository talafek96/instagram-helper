# instagram-helper — Tal's Instagram expert

Fork of [William-Gao/instagram-mcp](https://github.com/William-Gao/instagram-mcp) (remote `upstream`),
kept at `talafek96/instagram-helper` (remote `origin`). The Instagram counterpart of
`~/projects/whatsapp-helper`. It is registered as the user-scope MCP server `instagram`, so its
tools (`mcp__instagram__*`) work from every project.

## Who this serves
Tal's business account **@through_tals_lens** (cosplay photography). Instagram voice and caption
style live in `~/projects/insta-buddy` (`references/style-guide.md`). Shoot planning lives in
`~/projects/photoslots`.

## Rules
- **Never send a DM, comment reply, or post without Tal's explicit approval of the exact text**
  (or exact image + caption). Draft, show it, wait for a clear yes. Reading is always fine.
- Tal does not read Hebrew comfortably in the terminal: talk to him in English; put Hebrew
  drafts in a plain `.txt` opened in TextEdit and give the full absolute path.
- DM content and cosplayer personal data never go into git.
- The token lives only in `.env` here (gitignored). Never print it, commit it, or paste it anywhere.

## How it connects
- Official Instagram API with **Instagram Login** (`graph.instagram.com`, token starts `IGAA`).
  No Facebook Page, no private API, no ban risk.
- DMs need `instagram_business_manage_messages`. **Standard Access (no App Review) is enough**
  because Tal's own account has a role on his Meta app (Meta docs, Conversations API, checked
  2026-11-19). Upstream's README says App Review is needed; that applies only to other people's accounts.
- Limits: only the **20 most recent messages** per conversation; Requests-folder threads idle
  30+ days are hidden; sending works only within 24 h of the person's last message.
- Long-lived tokens last 60 days. `refresh_access_token` extends them; refresh before expiry.
- Run: `uv --directory ~/projects/instagram-helper run instagram-mcp` (that's what the MCP entry does).

## Setup (one-time, Tal does the clicks)
1. Instagram app: @through_tals_lens must be a Professional account (Business or Creator).
   Settings → Messages and story replies → Message controls → **Connected tools → Allow access to messages: on**.
2. developers.facebook.com → My Apps → Create app → use case "Manage messaging & content on Instagram".
3. App → Instagram → API setup with Instagram login → add @through_tals_lens as an Instagram tester
   (accept the invite in Instagram: Settings → Website permissions → Apps and websites → Tester invites)
   → **Generate token** for the account.
4. Put the token in `~/projects/instagram-helper/.env` as `INSTAGRAM_ACCESS_TOKEN=...`
   (plus `INSTAGRAM_APP_ID` / `INSTAGRAM_APP_SECRET` from the app's Instagram settings, for refresh).
5. Restart Claude Code, then check with `validate_access_token` and `get_conversations`.

## Working on the code
Upstream's contribution notes are in `README.md`. Keep Tal-specific changes small so upstream merges
stay easy: `git fetch upstream && git merge upstream/main`.
