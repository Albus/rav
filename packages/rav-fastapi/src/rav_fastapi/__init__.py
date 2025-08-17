from typing import Any

from starlette.requests import HTTPConnection


async def state(request: HTTPConnection) -> dict[str,Any]:
    return request.scope["state"]