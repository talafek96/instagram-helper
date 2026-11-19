---
name: feedback-secrets
type: feedback
description: Where tokens go and how never to leak them
---
Every token is saved in **both** this repo's gitignored `.env` and
`/Users/talafek/Library/CloudStorage/OneDrive2-Personal/Documents/api_keys.txt`
(`Label:` line, value on the next line). Copy tokens via the clipboard (`pbpaste` into the files),
show at most the first 6 chars, then clear the clipboard. **Never print api_keys.txt**: values sit on
their own lines, so `key=value` masking doesn't hide them (that leaked all keys once, 2026-11-19).
Tokens are URL params, so keep httpx request logging off.
