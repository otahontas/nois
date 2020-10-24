# from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret

from pathlib import Path

config = Config(".env")

# Testing & development variales
TESTING = config("TESTING", cast=bool, default=False)
DEBUG = config("DEBUG", cast=bool, default=False)

# Database
EDGEDB_HOST = config("EDGEDB_HOST", cast=str, default="db")
EDGEDB_USER = config("EDGEDB_USER", cast=str, default="edgedb")
EDGEDB_DB = config("EDGEDB_DB", cast=str, default="edgedb")

# Files
FILE_API_FOLDER = config(
    "FILE_API_FOLDER", default=Path(__file__).parent.parent.absolute() / "files"
)
