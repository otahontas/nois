from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.graphql import GraphQLApp
from graphene import ObjectType, String, Schema

from .graphql.schema import Query

routes = [
    Route('/', GraphQLApp(
        schema=Schema(query=Query),
        executor_class=AsyncioExecutor
    ))
]

app = Starlette(routes=routes)
