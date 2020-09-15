from starlette.applications import Starlette
from starlette.routing import Route

from .gino import db
from .graphql import graphql_app

routes = [Route("/graphql", graphql_app)]


def get_app():
    app = Starlette(routes=routes)
    db.init_app(app)
    return app
