from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from server.graphql import graphql_app
from server.api import api_routes

from server.config import DEBUG

from server.database import init_db, create_pool, close_pool


async def homepage(request):
    return JSONResponse({"hello": "world"})


routes = [Route("/graphql", graphql_app), Mount("/api", routes=api_routes)]

app = Starlette(
    routes=routes,
    debug=DEBUG,
    on_startup=[init_db, create_pool],
    on_shutdown=[close_pool],
)
