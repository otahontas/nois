from starlette.routing import Route
from starlette.schemas import SchemaGenerator

from .api import add_file, stream_file
from ..config import FILE_API_FOLDER
from pathlib import Path

schemas = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Nois file API", "version": "1.0"}}
)


def openapi_schema(request):
    return schemas.OpenAPIResponse(request=request)


file_api_routes = [
    Route("/schema", openapi_schema, include_in_schema=False),
    Route("/{filename}", stream_file, methods=["GET"]),
    Route("/", add_file, methods=["POST"]),
]
