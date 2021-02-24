from __future__ import annotations

import strawberry
from strawberry.asgi import GraphQL

from server.graphql.queries.messages import get_messages, get_message
from server.graphql.types.message import Message


@strawberry.type
class Query:
    messages: list[Message] = strawberry.field(resolver=get_messages)
    message: Message = strawberry.field(resolver=get_message)


graphql_app = GraphQL(strawberry.Schema(query=Query))
