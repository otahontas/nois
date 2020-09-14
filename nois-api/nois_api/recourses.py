from __future__ import annotations

import typing
from dataclasses import dataclass

import edgedb


@dataclass
class EdgeDBConnection:
    dsn: typing.Optional[str] = None
    host: typing.Optional[str] = None
    port: int = 5656
    admin: typing.Optional[bool] = False
    user: typing.Optional[str] = None
    password: typing.Optional[str] = None
    database: typing.Optional[str] = None
    timeout: int = 60

    async def connect_async_pool(
        self,
        connection: typing.Optional[EdgeDBConnection] = None,
    ) -> edgedb.AsyncIOConnection:
        if not self.pool:
            self.pool = await edgedb.create_async_pool(
                dsn=self.dsn,
                host=self.host,
                port=self.port,
                admin=bool(self.admin),
                user=self.user,
                password=self.password,
                database=self.database,
                timeout=self.timeout,
                min_size=self.pool_min_size,
                max_size=self.pool_max_size,
            )
        return await self.pool.acquire()
