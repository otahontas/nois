from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from graphene import Schema
from .queries import Query
from .mutations import Mutation

graphql_app = GraphQLApp(
    schema=Schema(query=Query, mutation=Mutation),
    executor_class=AsyncioExecutor,
)
