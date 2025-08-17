from typing import Any, AsyncGenerator, Annotated, Literal, TypedDict, ReadOnly

import aioodbc
from fastapi import Depends

__all__ = [r'Connection',r'Cursor', r'Offset', r'Pool', r'State']

import rav_fastapi


class State(TypedDict, total=True):
    pool: ReadOnly[aioodbc.Pool]


# noinspection PyShadowingNames
async def __db_pool(state: Annotated[State, Depends(rav_fastapi.state)]) -> aioodbc.Pool:
    return state["pool"]



Pool = Annotated[aioodbc.Pool, Depends(__db_pool)]

async def __db_connection(pool: Pool) -> AsyncGenerator[aioodbc.Connection, Any]:
    async with pool.acquire() as conn:
        try:
            yield conn
        finally:
            pass

Connection = Annotated[aioodbc.Connection, Depends(__db_connection)]

async def __db_cursor(conn: Connection) -> AsyncGenerator[aioodbc.Cursor, Any]:
    async with conn.cursor() as cursor:
        try:
            yield cursor
        finally:
            pass

Cursor = Annotated[aioodbc.Cursor, Depends(__db_cursor)]

async def __time_offset(db: Connection) -> Literal[0,2000]:
    async with db.cursor() as cursor:
        return await (await cursor.execute("select top(1) Offset from _YearOffset")).fetchval()

Offset = Annotated[Literal[0,2000], Depends(__time_offset)]