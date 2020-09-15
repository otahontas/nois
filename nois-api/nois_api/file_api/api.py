from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, StreamingResponse
from starlette.exceptions import HTTPException
from ..config import FILE_API_FOLDER
import aiofiles
from pathlib import Path


async def stream_file(request: Request) -> StreamingResponse:
    """Get single video as streamed response"""
    filename = request.path_params["filename"]
    path_to_file = Path(FILE_API_FOLDER) / filename
    print(path_to_file)
    if not path_to_file:
        raise HTTPException(status_code=404)

    async def stream_file(path_to_file: str, blocksize: int = 1024 * 256):
        async with aiofiles.open(path_to_file, mode="rb") as file:
            while chunk := await file.read(blocksize):
                yield chunk

    return StreamingResponse(
        stream_file(str(path_to_file))
    )

async def add_file(self, request: Request) -> JSONResponse:
    form = await request.form()
    filename = form["upload_video"].filename
    contents = await form["upload_video"].read()
    async with aiofiles.open(
        f"{FILE_API_FOLDER}/{filename}", "wb"
    ) as new_file:
        written_bytes = await new_file.write(contents)
        if written_bytes != len(contents):
            raise HTTPException(
                status_code=400, contents="Couldn't save file to server."
            )
    return JSONResponse({"filename": filename}, status_code=201)
