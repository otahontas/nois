from starlette.applications import Starlette
from starlette.routing import Route
from nois_api.graphql import graphql_app

from nois_api.config import DEBUG

routes = [Route("/graphql", graphql_app)]


def get_app():
    app = Starlette(routes=routes, debug=DEBUG)
    return app
