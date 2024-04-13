from typing import Protocol

from modules.common.application.dto import TrafficDTO


class AIGatewayPort(Protocol):
    async def insert_bulk(self, *, traffic_list: list[TrafficDTO]) -> list[TrafficDTO]:
        raise NotImplementedError

    async def get_ai_results(self) -> list[TrafficDTO]:
        raise NotImplementedError
