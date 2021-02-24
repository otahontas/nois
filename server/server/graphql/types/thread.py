from __future__ import annotations

from strawberry import type, ID

from server.graphql.types.message import Message
from server.graphql.types.user import User


@type
class Thread:
    id: ID
    createdAt: str
    messages: list[Message]
    postedBy: User
    title: str
