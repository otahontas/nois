from server.config import FILE_API_FOLDER
from starlette.datastructures import UploadFile
from starlette.responses import FileResponse
from typing import Union
import aiofiles


def init_file_api_folder():
    # return true // false here depending on success
    FILE_API_FOLDER.mkdir(parents=True, exist_ok=True)


# TODO: we should raise exceptions instead of just logging


async def open_file(filename: str) -> Union[FileResponse, None]:
    path_to_file = FILE_API_FOLDER / filename
    if not path_to_file.exists():
        # Log here that writing not possible since file exists
        return None
    return FileResponse(path_to_file)


async def save_file(filename: str, file: UploadFile) -> bool:
    content_to_write = await file.read()

    path_to_file = FILE_API_FOLDER / filename
    if path_to_file.exists():
        # Log here that writing not possible since file exists
        return False

    async with aiofiles.open(str(path_to_file), "wb") as new_file:
        written_bytes = await new_file.write(content_to_write)
        if written_bytes != len(content_to_write):
            # Log here that writing was not successful
            return False
    return True


async def delete_file(filename: str) -> bool:
    path_to_file = FILE_API_FOLDER / filename

    try:
        path_to_file.unlink()
    except FileNotFoundError:
        # Log here that deleteing was not successful since file was not found
        return False

    return True
