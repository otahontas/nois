from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.graphql import GraphQLApp
from gino.ext.starlette import Gino
from graphene import ObjectType, String, Schema

from .graphql.queries import Query
from .graphql.mutations import Mutation

routes = [
    Route('/', GraphQLApp(
        schema=Schema(query=Query, mutation=Mutation),
        executor_class=AsyncioExecutor
    ))
]

app = Starlette(routes=routes)
db = Gino(app, user="nois", password="nois", database="nois")
