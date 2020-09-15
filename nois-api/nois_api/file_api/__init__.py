from starlette.routing import Route

from .api import add_file, stream_file

file_api_routes = [
    Route('/', add_file, methods=["POST"]),
    Route('/{filename}', stream_file, methods=["GET"]),
]
