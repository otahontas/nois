from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.graphql import GraphQLApp
from graphene import Schema

from .graphql.queries import Query
from .graphql.mutations import Mutation
from .gino import db

routes = [
    Route(
        "/",
        GraphQLApp(
            schema=Schema(query=Query, mutation=Mutation),
            executor_class=AsyncioExecutor,
        ),
    )
]


def get_app():
    app = Starlette(routes=routes)
    db.init_app(app)
    return app
