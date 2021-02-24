from __future__ import annotations
from strawberry import type, ID

from .message import Message


@type
class User:
    id: ID
    email: str
    messages: list[Message]
