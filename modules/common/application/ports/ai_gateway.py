from typing import Protocol

from modules.common.application.dto import TrafficDTO


class AIGatewayPort(Protocol):
    async def insert(self, *, traffic: TrafficDTO) -> TrafficDTO:
        raise NotImplementedError

    async def get_ai_results(self) -> list[TrafficDTO]:
        raise NotImplementedError
