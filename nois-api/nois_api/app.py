from starlette.applications import Starlette
from starlette.routing import Route, Mount

from .gino import db
from .graphql import graphql_app
from .file_api import file_api_routes, init_file_api_folder

from .config import GRAPHQL_API_BASE_URL, FILE_API_BASE_URL, DEBUG

routes = [
    Route("/graphql", graphql_app, name="graphql"),
    Mount("/files", routes=file_api_routes, name="files"),
]


def get_app():
    app = Starlette(routes=routes, on_startup=[init_file_api_folder], debug=DEBUG)
    db.init_app(app)
    return app
