from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, StreamingResponse
from starlette.exceptions import HTTPException
from ..config import FILE_API_FOLDER, FILE_API_DEFAULT_CHUNK_SIZE
from pathlib import Path
import aiofiles
from uuid import uuid4


async def stream_file(request: Request) -> StreamingResponse:
    """
    description: Get single file by id
    responses:
      200:
        description: Return streamed response of single file
      404:
        description: Requested file doesn't exist
    """

    filename = request.path_params["filename"]
    path_to_file = FILE_API_FOLDER / filename

    if not path_to_file.exists():
        raise HTTPException(status_code=404)

    async def stream_file(
        path_to_file: str, chunk_size: int = FILE_API_DEFAULT_CHUNK_SIZE
    ):
        async with aiofiles.open(path_to_file, mode="rb") as file:
            while chunk := await file.read(chunk_size):
                yield chunk

    return StreamingResponse(stream_file(str(path_to_file)))


async def add_file(request: Request) -> JSONResponse:
    """
    description: Upload file
    responses:
      201:
        description: Return JSON for filename after successful upload
        examples:
          {"filename": "00ee0344-5291-41ca-ae62-a7c90aad577e"}
      400:
        description: Error happened file uploading
    """
    form = await request.form()
    contents = await form["upload_file"].read()

    while (path_to_file := FILE_API_FOLDER / str(uuid4())).exists():
        continue

    async with aiofiles.open(str(path_to_file), "wb") as new_file:
        written_bytes = await new_file.write(contents)
        if written_bytes != len(contents):
            raise HTTPException(
                status_code=400, contents="Couldn't save file to server."
            )
    return JSONResponse({"filename": path_to_file.name}, status_code=201)


async def delete_file(request: Request) -> None:
    """
    description: Delete single file by id
    responses:
      204:
        description: Return no content after successful deletion
      404:
        description: Requested file doesn't exist
    """

    filename = request.path_params["filename"]
    path_to_file = FILE_API_FOLDER / filename

    try:
        path_to_file.unlink()
    except FileNotFoundError:
        raise HTTPException(status_code=404)

    raise HTTPException(status_code=204)
