from typing import AsyncGenerator, Optional
import asyncio

from edgedb import AsyncIOConnection, AsyncIOPool, create_async_pool, async_connect
from pathlib import Path

from nois_api.config import EDGEDB_HOST, EDGEDB_USER, EDGEDB_DB
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

pool: AsyncIOPool


async def create_pool() -> None:
    global pool
    pool = await create_async_pool(
        host=EDGEDB_HOST,
        database=EDGEDB_DB,
        user=EDGEDB_USER,
    )


async def close_pool() -> None:
    await pool.aclose()


async def get_connection() -> AsyncGenerator[AsyncIOConnection, None]:
    try:
        connection = await pool.acquire()
        yield connection
    finally:
        await pool.release(connection)


max_tries = 60 * 5  # 5 minutes
wait_seconds = 1
schema_file = Path(__file__).parent / "schema.esdl"


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
    logger.info("Initializing service")
    con = await check_db()
    if con:
        with open(schema_file) as f:
            schema = f.read()
        async with con.transaction():
            await con.execute(f"""START MIGRATION TO {{ {schema} }}""")
            await con.execute("""POPULATE MIGRATION""")
            await con.execute("""COMMIT MIGRATION""")
        logger.info("Service finished initializing")
