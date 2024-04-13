import asyncio
from logging import getLogger

from modules.common.adapters.errors import UoWError
from modules.common.application import ports
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

logger = getLogger(__name__)


class UoW(ports.UoWPort):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def __aenter__(self) -> "UoW":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.rollback()
        task = asyncio.create_task(self._session.close())
        await asyncio.shield(task)
        if exc_type:
            logger.error("Handled exception: %s - %s", exc_type, exc_val)
        if issubclass(type(exc_val), SQLAlchemyError):
            raise UoWError(
                f"Integrity error on the database side: {type(exc_val)}"
            ) from exc_val
