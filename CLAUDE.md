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
- Tokens live in `.env` here (gitignored) AND in the OneDrive api_keys.txt below. Never print, commit or paste them.

## Memory (self-improving)
Durable lessons live in **`memory/`**, indexed by **`memory/MEMORY.md`**; `.claude/hooks/inject-memory.sh`
injects the index, `project-status.md` and all `feedback-*.md` at every session start (also after compaction).
- When Tal corrects you, confirms an approach, or you learn something durable about Meta/Instagram:
  update memory **in the same turn**. Edit the matching file instead of adding a near-duplicate;
  rewrite superseded rules. One fact per file, kebab-case name = frontmatter `name:`,
  `type:` user / feedback / project / reference. Feedback files: the rule, **Why**, **How to apply**.
- Keep `project-status.md` current whenever something changes state.
- Commit and push memory with the work that taught it.
- Never store DM contents, cosplayer personal data or tokens in memory.
- Other projects use these tools via MCP; the server's `instructions` tell them to read and update
  this folder, so lessons learned elsewhere still land here.

## How it connects (as set up 2026-11-19)
- Meta app **Tals Lens Helper** (ID 972224512280829), owned by business portfolio **Through Tals Lens**
  (1761668101576010). Meta no longer offers "Instagram login" to new apps, only **Unified login**:
  one **system-user token (EAA..., never expires)** per Instagram account, calls go to
  `graph.facebook.com/{ig-user-id}`. Our patch: `IG_ACCOUNTS` in `.env` turns this mode on, `"me"`
  paths become the IG user id, tools `list_accounts` / `use_account` switch accounts.
- `.env` keys: `IG_ACCOUNTS`, `IG_DEFAULT_ACCOUNT`, `IG_USER_ID_<NAME>`, `IG_TOKEN_<NAME>`.
  Every token is **also** saved in `/Users/talafek/Library/CloudStorage/OneDrive2-Personal/Documents/api_keys.txt`.
  Never print that file (one secret per line).
- Accounts: `through_tals_lens` = 17841476210183578; `talafek96` = 17841401771590540 (switched to Creator 2026-11-19).
- New token: the account must be (1) Professional, (2) added to the portfolio in Business Suite ->
  Instagram accounts, (3) an accepted Instagram Tester (instagram.com/accounts/manage_access -> Tester
  invites); then app -> Use cases -> Instagram API -> API setup with Unified login -> Generate token.
  Meta's asset/login popups open outside the Chrome tab group, so Tal clicks those.
- DMs also need the phone-app switch **Connected tools -> Allow access to messages**, otherwise Meta
  returns "(#200) The account owner has disabled access to Instagram Direct Messaging Outside of Instagram App".
- Limits: only the **20 most recent messages** per conversation; sending only within 24 h of their last message.
- `mcp` is pinned `<2` (2.x renamed FastMCP). httpx INFO logging is silenced because URLs carry the token.
- Run: `uv --directory ~/projects/instagram-helper run instagram-mcp` (what the user-scope MCP entry does).

## Working on the code
Upstream's contribution notes are in `README.md`. Keep Tal-specific changes small so upstream merges
stay easy: `git fetch upstream && git merge upstream/main`.
