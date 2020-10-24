from typing import AsyncGenerator

from edgedb import AsyncIOConnection, AsyncIOPool, create_async_pool

from nois_api.config import EDGEDB_HOST, EDGEDB_USER, EDGEDB_DB

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

