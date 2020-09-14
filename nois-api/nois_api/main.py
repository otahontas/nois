from graphql.execution.executors.asyncio import AsyncioExecutor
import graphene
from starlette.graphql import GraphQLApp
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.routing import Route
import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    async def resolve_hello(self, info, name):
        # We can make asynchronous network calls here.
        return "Hello " + name


routes = [
    # We're using `executor_class=AsyncioExecutor` here.
    Route(
        "/",
        GraphQLApp(schema=graphene.Schema(query=Query), executor_class=AsyncioExecutor),
    )
]

app = Starlette(routes=routes)
