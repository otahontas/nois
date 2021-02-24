from __future__ import annotations

from strawberry import type, ID


@type
class Message:
    id: ID
    title: str
    recordingUrl: str
    createdAt: str
