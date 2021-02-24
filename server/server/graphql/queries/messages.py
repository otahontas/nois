from __future__ import annotations

from typing import Optional

from strawberry import ID

from server.graphql.types.message import Message

example_list = [
    Message(
        id="1234",
        title="Jeeps",
        recordingUrl="https://janna.com/jeejee",
        createdAt="2020-12-12",
    ),
    Message(
        id="5678",
        title="juuh",
        recordingUrl="https://janna.com/joojoo",
        createdAt="2020-12-12",
    ),
    Message(
        id="91011",
        title="jou",
        recordingUrl="https://janna.com/juujuu",
        createdAt="2020-12-12",
    ),
]


async def get_messages() -> list[Message]:
    return example_list


async def get_message(message_id: ID) -> Optional[Message]:
    try:
        return next(message for message in example_list if message.id == message_id)
    except StopIteration:
        return None
