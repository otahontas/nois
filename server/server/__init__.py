from starlette.applications import Starlette
from starlette.routing import Route

from .graphql import graphql_app
from .config import DEBUG

routes = [
    Route("/graphql", graphql_app, name="graphql"),
]

app = Starlette(
    routes=routes,
    debug=DEBUG,
)
