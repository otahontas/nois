from starlette.config import Config

from pathlib import Path

import logging

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

# Logging
logging_format = (
    "[%(asctime)s][%(name)s][%(process)d %(processName)s]"
    "[%(levelname)-8s](L:%(lineno)s) %(funcName)s: %(message)s"
)
logging.basicConfig(format=logging_format, datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger("server")
logger.setLevel(logging.INFO)
