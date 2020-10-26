from typing import Optional
import asyncio

from edgedb import AsyncIOConnection, async_connect, create_async_pool, AsyncIOPool
from pathlib import Path

from server.config import EDGEDB_HOST, EDGEDB_USER, EDGEDB_DB
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1
schema_file = Path(__file__).parent / "schema.esdl"


pool: AsyncIOPool


async def create_pool() -> None:
    global pool
    pool = await create_async_pool(
        host=EDGEDB_HOST,
        database=EDGEDB_DB,
        user=EDGEDB_USER,
    )


async def close_pool() -> None:
    global pool
    await pool.aclose()


async def get_pool() -> AsyncIOPool:
    global pool
    return pool


async def check_db() -> Optional[AsyncIOConnection]:
    for attempt in range(max_tries):
        try:
            con = await async_connect(
                host=EDGEDB_HOST,
                database=EDGEDB_DB,
                user=EDGEDB_USER,
            )
            # Try to create session to check if DB is awake
            await con.execute("SELECT 1")
            return con
        except Exception as e:
            if attempt < max_tries - 1:
                logger.error(
                    f"""{e}
Attempt {attempt + 1}/{max_tries} to connect to database, waiting {wait_seconds}s."""
                )
                await asyncio.sleep(wait_seconds)
            else:
                raise e
    return None


async def init_db() -> None:
    logger.info("Performing database migrations")
    con = await check_db()
    if con:
        with open(schema_file) as f:
            schema = f.read()
        async with con.transaction():
            await con.execute(f"""START MIGRATION TO {{ {schema} }}""")
            await con.execute("""POPULATE MIGRATION""")
            await con.execute("""COMMIT MIGRATION""")
        logger.info("Database initialized and migrations committed")
