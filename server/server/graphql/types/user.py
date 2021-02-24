from __future__ import annotations
from strawberry import type, ID


@type
class User:
    id: ID
    createdAt: str
