from typing import Any, AsyncGenerator, Annotated, Literal

from aioodbc import Pool, Connection, Cursor
from fastapi import Depends

__all__ = [r'Connection',r'Cursor', r'Offset']


async def __db_connection(pool: Pool) -> AsyncGenerator[Connection, Any]:
    async with pool.acquire() as conn:
        try:
            yield conn
        finally:
            pass

Connection = Annotated[Connection, Depends(__db_connection)]

async def __db_cursor(conn: Connection) -> AsyncGenerator[Cursor, Any]:
    async with conn.cursor() as cursor:
        try:
            yield cursor
        finally:
            pass

Cursor = Annotated[Cursor, Depends(__db_cursor)]

async def __time_offset(db: Connection) -> Literal[0,2000]:
    async with db.cursor() as cursor:
        return await (await cursor.execute("select top(1) Offset from _YearOffset")).fetchval()

Offset = Annotated[int, Depends(__time_offset)]