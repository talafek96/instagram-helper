---
name: reference-meta-setup
type: reference
description: Meta app/portfolio/token setup for the Instagram helper and the quirks hit on the way
---
- Meta app **Tals Lens Helper** 972224512280829 (dev mode, no App Review needed for own accounts).
  Business portfolio **Through Tals Lens** 1761668101576010 (unverified; verification only matters
  for other people's data). Login configuration 1166474629194648 (system-user token, never expires).
- Accounts: through_tals_lens 17841476210183578, talafek96 17841401771590540 (made Creator, so public).
- Add an account: make it Professional → Business Suite → Settings → Instagram accounts → Add
  (login popup) → app Roles → Add People → Instagram Tester → accept at
  instagram.com/accounts/manage_access (Tester invites tab; the phone app often doesn't show it) →
  app → Use cases → Instagram API → API setup with Unified login → Generate token (asset popup:
  pick the IG account, no ad account) → "I understand" → Copy.
- Quirks: new apps get only Unified login (EAA tokens on graph.facebook.com, no /me for IG users,
  no `account_type` field). App names can't contain "instagram"/"insta"/"gram". Meta popups open
  outside the Chrome extension's tab group. A personal IG account fails to add with a generic
  "Sorry, something went wrong". DMs need the phone-app switch Connected tools → Allow access to
  messages, else error #200 "disabled access to Instagram Direct Messaging Outside of Instagram App".
- mcp 2.x broke the server (FastMCP renamed): pinned `mcp<2`.
