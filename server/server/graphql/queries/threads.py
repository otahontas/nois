from __future__ import annotations

from typing import Optional

from strawberry import ID

from server.graphql.types.thread import Thread
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

threads = [
    Thread(
        id="3a8609a5-58c1-40c7-9016-66dc83245be8",
        createdAt="2011-11-04 00:05:23.283+00:00",
        messages=[],
        postedBy=users[0],
        title="ebin juttu kävi kampis"
    ),
    Thread(
        id="ed91ddee-d038-4c82-9028-87313ddf0bef",
        createdAt="2011-11-04 00:08:.283+00:00",
        messages=[],
        postedBy=users[0],
        title="huoh en jaksa enää koronaa"
    ),
    Thread(
        id="91011",
        createdAt="2011-11-04 00:12:23.283+00:00",
        messages=[],
        postedBy=users[1],
        title="pääsykoecasesta settiä",
    ),
]


async def all_threads() -> list[Thread]:
    return threads


async def thread(thread_id: ID) -> Optional[Thread]:
    try:
        return next(t for t in threads if t.id == thread_id)
    except StopIteration:
        return None
