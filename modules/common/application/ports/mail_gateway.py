from typing import Protocol

from modules.common.application.dto import MailDTO


class MailGatewayPort(Protocol):
    async def insert(self, *, mail: MailDTO) -> MailDTO:
        raise NotImplementedError
