from starlette.applications import Starlette
from starlette.routing import Route, Mount
from server.graphql import graphql_app
from server.api import api_routes

from server.config import DEBUG

from server.database import db
from server.file_io import init_file_api_folder

routes = [Route("/graphql", graphql_app), Mount("/api", routes=api_routes)]

app = Starlette(
    routes=routes,
    debug=DEBUG,
    on_startup=[db.initialize_database, init_file_api_folder],
    on_shutdown=[db.close_pool],
)
