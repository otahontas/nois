from starlette.applications import Starlette
from starlette.routing import Route, Mount

from .gino import db
from .graphql import graphql_app
from .file_api import file_api_routes

from .config import GRAPHQL_API_BASE_URL, FILE_API_BASE_URL

routes = [Route(GRAPHQL_API_BASE_URL, graphql_app), Mount(FILE_API_BASE_URL, routes=file_api_routes)]


def get_app():
    app = Starlette(routes=routes)
    db.init_app(app)
    return app
