from __future__ import annotations

from starlette.applications import Starlette
from starlette.routing import Route

from .graphql import graphql_app
from .config import DEBUG
from .database import initialize_database

routes = [
    Route("/graphql", graphql_app, name="graphql"),
]

app = Starlette(routes=routes, debug=DEBUG, on_startup=[initialize_database])
