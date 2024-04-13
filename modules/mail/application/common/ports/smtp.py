from typing import Protocol

from modules.common.application.dto import MailDTO


class SMTPPort(Protocol):
    async def send_messages(self, *, mails: list[MailDTO]) -> list[MailDTO]:
        raise NotImplementedError
