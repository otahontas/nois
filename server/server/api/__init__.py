from __future__ import annotations

from server.file_io import open_file
from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.routing import Route
from starlette.exceptions import HTTPException


async def get_file(request: Request) -> FileResponse:
    """
    description: Get single file by id
    responses:
      200:
        description: Return single file
      404:
        description: Requested file doesn't exist
    """

    filename = str(request.path_params["filename"])
    response = await open_file(filename)
    if not response:
        raise HTTPException(status_code=404)
    return response


api_routes = [Route("/files/{filename}", get_file, methods=["GET"], name="get_file")]
