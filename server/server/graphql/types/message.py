from __future__ import annotations

from strawberry import type, ID

from server.graphql.types.user import User


@type
class Message:
    id: ID
    createdAt: str
    recordingUrl: str
    postedBy: User
