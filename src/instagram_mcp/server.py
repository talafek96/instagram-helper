from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from typing import Any

from mcp.server.fastmcp import FastMCP

from .client import FBGraphClient, InstagramAPIError, InstagramClient
from .config import Config

logger = logging.getLogger(__name__)
# httpx logs full request URLs at INFO, and the access token is a URL parameter.
logging.getLogger("httpx").setLevel(logging.WARNING)


_INSTRUCTIONS = """Tal's Instagram helper (@through_tals_lens, @talafek96). Its memory lives in
~/projects/instagram-helper/memory/ (index: MEMORY.md).
- BEFORE the first Instagram tool call in a session, read MEMORY.md and every feedback-*.md there.
- NEVER send a DM, comment reply or post without Tal's explicit approval of the exact text.
- When Tal corrects or confirms how Instagram work should be done, or you learn a durable fact about
  the API/setup, update that memory folder right away (edit the matching file, don't duplicate; one
  fact per file; feedback-*: rule + Why + How to apply), update MEMORY.md, then commit and push
  ~/projects/instagram-helper. Never put DM contents, cosplayer personal data or tokens in memory.
- Accounts: list_accounts / use_account. Only the 20 latest messages per chat are readable."""

mcp = FastMCP("instagram-mcp", instructions=_INSTRUCTIONS)

_client: InstagramClient | None = None
_fb_client: FBGraphClient | None = None
_config: Config | None = None


def get_client() -> InstagramClient:
    global _client, _config
    if _client is None:
        _config = Config.from_env()
        _client = InstagramClient(_config)
    return _client


def use_account_(name: str) -> Config:
    """Switch every tool to another configured Instagram account (Unified-login mode)."""
    global _client, _fb_client, _config
    cfg = Config.from_env(name)
    _config, _client, _fb_client = cfg, InstagramClient(cfg), None
    return cfg


def get_fb_client() -> FBGraphClient | None:
    """Return a Facebook Graph API client if INSTAGRAM_FB_ACCESS_TOKEN is set, else None."""
    global _fb_client, _config
    if _config is None:
        get_client()
    assert _config is not None
    if not _config.has_fb_graph:
        return None
    if _fb_client is None:
        _fb_client = FBGraphClient(_config)
    return _fb_client


def get_config() -> Config:
    if _config is None:
        get_client()
    assert _config is not None
    return _config


def fb_required_error(feature: str) -> dict[str, Any]:
    return {
        "ok": False,
        "error": {
            "message": (
                f"{feature} requires Facebook Graph API access. Set "
                "INSTAGRAM_FB_ACCESS_TOKEN (EAA-prefixed Page access token) and "
                "INSTAGRAM_FB_IG_USER_ID (your IG Business Account ID) in your env. "
                "Call the `discover_fb_setup` tool with just the FB token to "
                "auto-find your IG Business Account ID. Full setup guide in the README."
            ),
            "type": "FBGraphTokenMissing",
        },
    }


def format_error(e: Exception) -> dict[str, Any]:
    if isinstance(e, InstagramAPIError):
        return {"ok": False, "error": e.to_dict()}
    return {"ok": False, "error": {"message": str(e), "type": type(e).__name__}}


@asynccontextmanager
async def safe_call():
    try:
        yield
    except InstagramAPIError as e:
        logger.warning("Instagram API error: %s", e)
        raise


# Trigger tool registrations from sub-modules
from .tools import (  # noqa: E402,F401
    auth,
    comments,
    discovery,
    hashtags,
    insights,
    media,
    messaging,
    publish,
)
