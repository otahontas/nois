from __future__ import annotations

import typing
import strawberry
from strawberry.asgi import GraphQL


async def get_books():
    return [
        Book(
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
        ),
    ]

@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


graphql_app = GraphQL(strawberry.Schema(query=Query))
