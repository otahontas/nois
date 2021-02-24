from __future__ import annotations

from typing import Optional

from strawberry import ID

from server.graphql.types.message import Message
from server.graphql.types.user import User

users = [
    User(
        id="22d911b6-09af-485d-99c9-dfe2d60b052b",
        createdAt="2011-11-03 00:02:23.283+00:00",

    ),
    User(
        id="602cc61e-4612-44cc-96aa-1039bdd3f4ba",
        createdAt="2011-11-02 00:01:23.283+00:00",
    )
]

messages = [
    Message(
        id="afaf10ee-0784-49b8-937e-6d49b9884689",
        createdAt="2011-11-02 00:01:23.283+00:00",
        recordingUrl="https://juuh.com/jeejee1.ogg",
        postedBy=users[0]
    ),
    Message(
        id="8e8107de-0288-4cb3-ba9f-de266eee30a6",
        createdAt="2011-11-02 00:01:23.283+00:00",
        recordingUrl="https://juuh.com/jeejee2.ogg",
        postedBy=users[0]
    ),
    Message(
        id="4f916520-0192-42a1-9277-31bff001e311",
        createdAt="2011-11-02 00:01:23.283+00:00",
        recordingUrl="https://janna.com/jeejee3.ogg",
        postedBy=users[1]
    ),
]


async def all_messages() -> list[Message]:
    return messages


async def message(message_id: ID) -> Optional[Message]:
    try:
        return next(m for m in messages if m.id == message_id)
    except StopIteration:
        pass
