from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret

from pathlib import Path, PurePath
import os

config = Config(".env")

# Testing & development variales
TESTING = config("TESTING", cast=bool, default=False)
DEBUG = config("DEBUG", cast=bool, default=False)

# Database
DB_DRIVER = config("DB_DRIVER", default="postgresql")
DB_HOST = config("DB_HOST", default=None)
DB_PORT = config("DB_PORT", cast=int, default=None)
DB_DATABASE = "nois_test" if TESTING else config("DB_DATABASE", default=None)
DB_USER = "nois_test" if TESTING else config("DB_USER", default=None)
DB_PASSWORD = (
    "nois_test" if TESTING else config("DB_PASSWORD", cast=Secret, default=None)
)
DB_DSN = config(
    "DB_DSN",
    cast=make_url,
    default=URL(
        drivername=DB_DRIVER,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    ),
)
DB_POOL_MIN_SIZE = config("DB_POOL_MIN_SIZE", cast=int, default=1)
DB_POOL_MAX_SIZE = config("DB_POOL_MAX_SIZE", cast=int, default=16)
DB_ECHO = config("DB_ECHO", cast=bool, default=False)
DB_SSL = config("DB_SSL", default=None)
DB_USE_CONNECTION_FOR_REQUEST = config(
    "DB_USE_CONNECTION_FOR_REQUEST", cast=bool, default=True
)
DB_RETRY_LIMIT = config("DB_RETRY_LIMIT", cast=int, default=1)
DB_RETRY_INTERVAL = config("DB_RETRY_INTERVAL", cast=int, default=1)

# File API
FILE_API_FOLDER = config(
    "FILE_API_FOLDER", default=Path(__file__).parent.parent.absolute() / "files"
)
FILE_API_DEFAULT_CHUNK_SIZE = config(
    "FILE_API_DEFAULT_BLOCKSIZE", cast=int, default=1024
)
FILE_API_BASE_URL = config("FILE_API_BASE_URL", cast=str, default="/files")

# Graphql API
GRAPHQL_API_BASE_URL = config("GRAPHQL_API_BASE_URL", cast=str, default="/graphql")
