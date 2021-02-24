from __future__ import annotations

from typing import Optional

from strawberry import ID

from server.database import fetch_thread
from server.graphql.types.thread import Thread
from server.graphql.types.message import Message
from server.graphql.types.user import User


async def all_threads() -> list[Thread]:
    return []


async def thread(thread_id: ID) -> Optional[Thread]:
    try:
        raw_thread, raw_messages = await fetch_thread(thread_id)
    except ValueError:
        return None
    messages = []
    base_url = "https://example.com"
    for raw_message in raw_messages:
        recording_uuid = raw_message["recording_uuid"]
        messages.append(
            Message(
                id=raw_message["id"],
                createdAt=raw_message["created_at"],
                recordingUrl=f"{base_url}/{recording_uuid}",
                postedBy=User(
                    id=raw_message["user_id"], createdAt=raw_message["created_at"]
                ),
            )
        )
    return Thread(
        id=raw_thread["id"],
        createdAt=raw_thread["created_at"],
        messages=messages,
        postedBy=User(id=raw_thread["user_id"], createdAt=raw_thread["created_at"]),
        title=raw_thread["title"],
    )
