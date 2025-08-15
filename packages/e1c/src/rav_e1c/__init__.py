from typing import AsyncIterator

from httpx import AsyncClient, AsyncHTTPTransport, URL

__all__ = [r'client']


async def client(url: str | URL, timeout=60) -> AsyncIterator[AsyncClient]:
    async with AsyncClient(
            base_url=url, default_encoding=r'utf-8-sig',
            verify=False, transport=AsyncHTTPTransport(
                verify=False, retries=3), timeout=timeout) as cl:
        yield cl
