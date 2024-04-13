from dataclasses import dataclass
from typing import Protocol, TypeVar

Req = TypeVar("Req", contravariant=True)
Resp = TypeVar("Resp", covariant=True)


@dataclass(frozen=True, kw_only=True)
class Request: ...


@dataclass(frozen=True, kw_only=True)
class Response: ...


class RequestHandler(Protocol[Req, Resp]):
    async def handle(self, request: Req) -> Resp: ...
