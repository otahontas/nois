from __future__ import annotations

from typing import Optional

import strawberry
from strawberry.asgi import GraphQL

from server.graphql.queries.threads import all_threads, thread
from server.graphql.types.thread import Thread


@strawberry.type
class Query:
    threads: list[Thread] = strawberry.field(resolver=all_threads)
    thread: Optional[Thread] = strawberry.field(resolver=thread)


graphql_app = GraphQL(strawberry.Schema(query=Query))
