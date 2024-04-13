from typing import Protocol


class UoWPort(Protocol):
    async def commit(self) -> None:
        raise NotImplementedError

    async def rollback(self) -> None:
        raise NotImplementedError

    async def __aenter__(self) -> "UoWPort":
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError
