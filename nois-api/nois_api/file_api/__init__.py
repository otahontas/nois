from starlette.routing import Route
from starlette.schemas import SchemaGenerator

from .api import add_file, stream_file, delete_file
from ..config import FILE_API_FOLDER
from pathlib import Path

schemas = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Nois file API", "version": "1.0"}}
)


def openapi_schema(request):
    return schemas.OpenAPIResponse(request=request)


def init_file_api_folder():
    FILE_API_FOLDER.mkdir(parents=True, exist_ok=True)


file_api_routes = [
    Route("/schema", openapi_schema, include_in_schema=False),
    Route("/{filename}", stream_file, methods=["GET"], name="stream_file"),
    Route("/{filename}", delete_file, methods=["DELETE"]),
    Route("/", add_file, methods=["POST"]),
]
