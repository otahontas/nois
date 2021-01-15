from typing import Optional, Callable, Any
import asyncio
from dataclasses import dataclass
from functools import wraps

from edgedb import create_async_pool, ClientConnectionError, AsyncIOPool
from pathlib import Path

from server.config import EDGEDB_HOST, EDGEDB_USER, EDGEDB_DB, logger


def auto_reconnect(func: Callable) -> Callable:
    @wraps(func)
    async def retry(*args: Any, **kwargs: Any) -> Any:
        """Retry given method for multiple times in increasing intervals."""
        max_attempts = 4
        timeout = 5

        for attempt in range(1, max_attempts + 1):
            try:
                return await func(*args, **kwargs)
            except (ClientConnectionError, ConnectionAbortedError) as error:
                if attempt == max_attempts:
                    logger.error(
                        f"Connection to database failed after {attempt} " "tries"
                    )
                    raise error
                logger.error(
                    f"Connection not successful, trying to reconnect."
                    f"Reconnection attempt number {attempt}, waiting "
                    f" for {timeout} seconds."
                )
                await asyncio.sleep(timeout)
                timeout *= 2
                continue

    return retry


@dataclass
class EdgeDBConnection:
    """Wrap connection stuff inside class."""

    host: str = EDGEDB_HOST
    database: str = EDGEDB_DB
    user: str = EDGEDB_USER
    migrate: bool = False
    pool: Optional[AsyncIOPool] = None
    schema_file: Path = Path(__file__).parent / "schema.esdl"
    close_timeout: int = 60

    @auto_reconnect
    async def create_pool(self) -> None:
        """Create pool, if not already created"""
        self.pool = await create_async_pool(
            host=self.host, database=self.database, user=self.user
        )

    async def close_pool(self) -> None:
        """Close pool, terminate if not possible in given time."""
        if self.pool:
            await asyncio.wait_for(self.pool.aclose(), timeout=self.close_timeout)

    async def get_pool(self) -> AsyncIOPool:
        """Returns connection pool, creates it if not created.

        To properly get and release connection, use with context manager, e.g.
        pool = db.get_pool()
        async with pool.acquire() as con:
            ...do things here
        """
        if not self.pool:
            await self.create_pool()
        return self.pool

    async def initialize_database(self) -> None:
        """Initialize the database connections and do migrations."""
        if self.migrate:
            logger.info("Starting database initialization and migrations.")
            pool = await self.get_pool()
            async with pool.acquire() as con:
                with open(self.schema_file) as f:
                    schema = f.read()
                async with con.transaction():
                    await con.execute(f"""START MIGRATION TO {{ {schema} }}""")
                    await con.execute("""POPULATE MIGRATION""")
                    await con.execute("""COMMIT MIGRATION""")
            logger.info("Database initialized and migrations committed.")


db = EdgeDBConnection()
