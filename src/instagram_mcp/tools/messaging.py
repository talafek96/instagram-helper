from __future__ import annotations

from typing import Any

from ..config import Config
from ..server import format_error, get_client, get_config, mcp, use_account_


@mcp.tool()
async def get_conversations(limit: int = 20) -> dict[str, Any]:
    """List Instagram DM conversations.

    Requires instagram_business_manage_messages. Standard Access (no App Review)
    is enough for your own account when it has a role on the Meta app.
    Only the 20 most recent messages of each conversation are readable.

    Args:
        limit: Number of conversations to return (1-100, default 20).
    """
    try:
        client = get_client()
        data = await client.get(
            "me/conversations",
            params={
                "platform": "instagram",
                "fields": "id,updated_time,participants,messages.limit(1){message,from,created_time}",
                "limit": max(1, min(100, limit)),
            },
        )
        return {"ok": True, **data}
    except Exception as e:
        return format_error(e)


@mcp.tool()
async def get_conversation_messages(conversation_id: str, limit: int = 25) -> dict[str, Any]:
    """List messages in a specific Instagram DM conversation.

    Requires instagram_business_manage_messages (Standard Access is enough for
    your own account). Meta only returns the 20 most recent messages.

    Args:
        conversation_id: ID from get_conversations.
        limit: Number of messages to return (1-100, default 25).
    """
    try:
        client = get_client()
        data = await client.get(
            conversation_id,
            params={
                "fields": (
                    "messages.limit(" + str(max(1, min(100, limit))) +
                    "){id,created_time,from,to,message,attachments}"
                )
            },
        )
        return {"ok": True, **data}
    except Exception as e:
        return format_error(e)


@mcp.tool()
async def send_dm(recipient_id: str, message: str) -> dict[str, Any]:
    """Send an Instagram DM.

    NEVER call this without the account owner's explicit approval of the exact
    message text in this conversation. Draft first, show it, wait for a yes.

    Requires instagram_business_manage_messages. Can only reply to users who
    have messaged you in the past 24 hours (24-hour window rule).

    Args:
        recipient_id: Instagram Scoped User ID (IGSID) of the recipient.
        message: Message text (max 1000 characters).
    """
    try:
        client = get_client()
        import json

        data = await client.post(
            "me/messages",
            data={
                "recipient": json.dumps({"id": recipient_id}),
                "message": json.dumps({"text": message}),
            },
        )
        return {"ok": True, **data}
    except Exception as e:
        return format_error(e)


@mcp.tool()
async def list_accounts() -> dict[str, Any]:
    """List the Instagram accounts this server can act as, and which one is active.

    Every other tool works on the active account. Switch with use_account.
    """
    try:
        return {"ok": True, "accounts": Config.accounts(), "active": get_config().account}
    except Exception as e:
        return format_error(e)


@mcp.tool()
async def use_account(name: str) -> dict[str, Any]:
    """Make another Instagram account active for all following tool calls.

    Args:
        name: An account name from list_accounts (e.g. "through_tals_lens", "talafek96").
    """
    try:
        cfg = use_account_(name)
        return {"ok": True, "active": cfg.account, "ig_user_id": cfg.ig_user_id}
    except Exception as e:
        return format_error(e)
