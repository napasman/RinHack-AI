from modules.common.adapters.persistence.tables import network_traffic_table
from modules.common.application.ports import AIGatewayPort
from modules.common.application.dto import TrafficDTO
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession


class AIGateway(AIGatewayPort):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def insert_bulk(self, *, traffic_list: list[TrafficDTO]) -> list[TrafficDTO]:
        values_list = [
            {
                "timestamp": traffic.timestamp,
                "source_ip": traffic.source_ip,
                "destination_ip": traffic.destination_ip,
                "protocol": traffic.protocol,
                "port": traffic.port,
                "packet_size": traffic.packet_size,
                "prediction": traffic.prediction,
            }
            for traffic in traffic_list
        ]

        statement = (
            insert(network_traffic_table)
            .returning(*network_traffic_table.columns)
            .values(values_list)
        )

        result = await self._session.execute(statement)

        return [
            TrafficDTO(
                id=traffic.id,
                timestamp=traffic.timestamp,
                source_ip=traffic.source_ip,
                destination_ip=traffic.destination_ip,
                protocol=traffic.protocol,
                port=traffic.port,
                packet_size=traffic.packet_size,
                prediction=traffic.prediction,
            )
            for traffic in result.all()
        ]

    async def get_ai_results(self) -> list[TrafficDTO]:
        statement = select(network_traffic_table)
        result = await self._session.execute(statement)
        rows = result.all()

        return [
            TrafficDTO(
                id=row.id,
                timestamp=row.timestamp,
                source_ip=row.source_ip,
                destination_ip=row.destination_ip,
                protocol=row.protocol,
                port=row.port,
                packet_size=row.packet_size,
                prediction=row.prediction,
            )
            for row in rows
        ]
