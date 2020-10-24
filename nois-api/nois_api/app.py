from starlette.applications import Starlette
from starlette.routing import Route, Mount
from nois_api.graphql import graphql_app
from nois_api.api import api_routes

from nois_api.config import DEBUG

routes = [Route("/graphql", graphql_app), Mount("/api", routes=api_routes)]


def get_app():
    app = Starlette(routes=routes, debug=DEBUG)
    return app
