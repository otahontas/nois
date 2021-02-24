from __future__ import annotations

from starlette.config import Config

import logging

config = Config(".env")

# Testing & development variables
TESTING = config("TESTING", cast=bool, default=False)
DEBUG = config("DEBUG", cast=bool, default=False)

# Database
DATABASE_URL = config("DATABASE_URL", cast=str, default="sqlite:///test.db")

# Logging
logging_format = (
    "[%(asctime)s][%(name)s][%(process)d %(processName)s]"
    "[%(levelname)-8s](L:%(lineno)s) %(funcName)s: %(message)s"
)
logging.basicConfig(format=logging_format, datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger("server")
logger.setLevel(logging.INFO)
