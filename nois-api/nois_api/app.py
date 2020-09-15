from starlette.applications import Starlette
from starlette.routing import Route, Mount

from .gino import db
from .graphql import graphql_app
from .file_api import file_api_routes

routes = [Route("/graphql", graphql_app), Mount("/files", routes=file_api_routes)]


def get_app():
    app = Starlette(routes=routes)
    db.init_app(app)
    return app
