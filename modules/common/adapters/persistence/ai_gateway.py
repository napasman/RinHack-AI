from modules.common.adapters.persistence.tables import network_traffic_table
from modules.common.application.ports import AIGatewayPort
from modules.common.application.dto import TrafficDTO
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession


class AIGateway(AIGatewayPort):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def insert(self, *, traffic: TrafficDTO) -> TrafficDTO:
        statement = insert(network_traffic_table).values(
            id=traffic.id,
            duration=traffic.duration,
            protocol_type=traffic.protocol_type,
            service=traffic.service,
            flag=traffic.flag,
            src_bytes=traffic.src_bytes,
            dst_bytes=traffic.dst_bytes,
            land=traffic.land,
            wrong_fragment=traffic.wrong_fragment,
            urgent=traffic.urgent,
            hot=traffic.hot,
            num_failed_logins=traffic.num_failed_logins,
            logged_in=traffic.logged_in,
            num_compromised=traffic.num_compromised,
            root_shell=traffic.root_shell,
            su_attempted=traffic.su_attempted,
            num_root=traffic.num_root,
            num_file_creations=traffic.num_file_creations,
            num_shells=traffic.num_shells,
            num_access_files=traffic.num_access_files,
            num_outbound_cmds=traffic.num_outbound_cmds,
            is_host_login=traffic.is_host_login,
            is_guest_login=traffic.is_guest_login,
            count=traffic.count,
            srv_count=traffic.srv_count,
            serror_rate=traffic.serror_rate,
            srv_serror_rate=traffic.srv_serror_rate,
            rerror_rate=traffic.rerror_rate,
            srv_rerror_rate=traffic.srv_rerror_rate,
            same_srv_rate=traffic.same_srv_rate,
            diff_srv_rate=traffic.diff_srv_rate,
            srv_diff_host_rate=traffic.srv_diff_host_rate,
            dst_host_count=traffic.dst_host_count,
            dst_host_srv_count=traffic.dst_host_srv_count,
            dst_host_same_srv_rate=traffic.dst_host_same_srv_rate,
            dst_host_diff_srv_rate=traffic.dst_host_diff_srv_rate,
            dst_host_same_src_port_rate=traffic.dst_host_same_src_port_rate,
            dst_host_srv_diff_host_rate=traffic.dst_host_srv_diff_host_rate,
            dst_host_serror_rate=traffic.dst_host_serror_rate,
            dst_host_srv_serror_rate=traffic.dst_host_srv_serror_rate,
            dst_host_rerror_rate=traffic.dst_host_rerror_rate,
            dst_host_srv_rerror_rate=traffic.dst_host_srv_rerror_rate,
            label=traffic.label,
            difficulty=traffic.difficulty,
            created_at=traffic.created_at,
        )

        result = await self._session.execute(statement)
        inserted_primary_key = result.inserted_primary_key[0]

        return TrafficDTO(id=inserted_primary_key, **traffic.__dict__)

    async def get_ai_results(self) -> list[TrafficDTO]:
        statement = select(network_traffic_table)
        result = await self._session.execute(statement)
        rows = result.all()

        return [
            TrafficDTO(
                id=row.id,
                duration=row.duration,
                protocol_type=row.protocol_type,
                service=row.service,
                flag=row.flag,
                src_bytes=row.src_bytes,
                dst_bytes=row.dst_bytes,
                land=row.land,
                wrong_fragment=row.wrong_fragment,
                urgent=row.urgent,
                hot=row.hot,
                num_failed_logins=row.num_failed_logins,
                logged_in=row.logged_in,
                num_compromised=row.num_compromised,
                root_shell=row.root_shell,
                su_attempted=row.su_attempted,
                num_root=row.num_root,
                num_file_creations=row.num_file_creations,
                num_shells=row.num_shells,
                num_access_files=row.num_access_files,
                num_outbound_cmds=row.num_outbound_cmds,
                is_host_login=row.is_host_login,
                is_guest_login=row.is_guest_login,
                count=row.count,
                srv_count=row.srv_count,
                serror_rate=row.serror_rate,
                srv_serror_rate=row.srv_serror_rate,
                rerror_rate=row.rerror_rate,
                srv_rerror_rate=row.srv_rerror_rate,
                same_srv_rate=row.same_srv_rate,
                diff_srv_rate=row.diff_srv_rate,
                srv_diff_host_rate=row.srv_diff_host_rate,
                dst_host_count=row.dst_host_count,
                dst_host_srv_count=row.dst_host_srv_count,
                dst_host_same_srv_rate=row.dst_host_same_srv_rate,
                dst_host_diff_srv_rate=row.dst_host_diff_srv_rate,
                dst_host_same_src_port_rate=row.dst_host_same_src_port_rate,
                dst_host_srv_diff_host_rate=row.dst_host_srv_diff_host_rate,
                dst_host_serror_rate=row.dst_host_serror_rate,
                dst_host_srv_serror_rate=row.dst_host_srv_serror_rate,
                dst_host_rerror_rate=row.dst_host_rerror_rate,
                dst_host_srv_rerror_rate=row.dst_host_srv_rerror_rate,
                label=row.label,
                difficulty=row.difficulty,
                created_at=row.created_at,
            )
            for row in rows
        ]
