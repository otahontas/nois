from starlette.routing import Route

from .api import add_file, stream_file
from ..config import FILE_API_FOLDER
from pathlib import Path

file_api_routes = [
    Route('/', add_file, methods=["POST"]),
    Route('/{filename}', stream_file, methods=["GET"]),
]
