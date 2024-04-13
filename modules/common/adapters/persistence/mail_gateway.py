from modules.common.adapters.persistence.tables import mail_table
from modules.common.application.ports import MailGatewayPort
from modules.common.application.dto import MailDTO
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession


class MailGateway(MailGatewayPort):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def insert(self, *, mail: MailDTO) -> MailDTO:
        statement = insert(mail_table).values(
            mail=mail.mail,
            created_at=mail.created_at,
        )
        result = await self._session.execute(statement)
        inserted_primary_key = result.inserted_primary_key[0]

        return MailDTO(
            mail_id=inserted_primary_key,
            mail=mail.mail,
            created_at=mail.created_at,
        )

    async def get_mails(self) -> list[MailDTO]:
        statement = select(mail_table)
        result = await self._session.execute(statement)
        rows = result.all()

        return [
            MailDTO(
                mail_id=row.mail_id,
                mail=row.mail,
                created_at=row.created_at,
            )
            for row in rows
        ]
