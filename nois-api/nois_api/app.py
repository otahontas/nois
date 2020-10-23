from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from starlette.applications import Starlette
from starlette.routing import Route

from .config import DEBUG

type_defs = """
    type Query {
        hello: String!
    }
"""
query = QueryType()


@query.field("hello")
def resolve_hello(*_):
    return "Hello world!"


schema = make_executable_schema(type_defs, query)

routes = [Route("/graphql", GraphQL(schema, debug=DEBUG))]


def get_app():
    app = Starlette(routes=routes, debug=DEBUG)
    return app
