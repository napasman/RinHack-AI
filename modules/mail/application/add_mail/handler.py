from modules.common.application import ports
from modules.common.application.dto import MailDTO
from modules.common.application.handlers import RequestHandler

from .request import AddMailRequest
from .response import AddMailResponse


class AddMailRequestHandler(
    RequestHandler[AddMailRequest, AddMailResponse]
):
    def __init__(
        self,
        mail_gateway: ports.MailGatewayPort,
        uow: ports.UoWPort,
    ) -> None:
        self._mail_gateway = mail_gateway
        self._uow = uow

    async def handle(self, request: AddMailRequest) -> AddMailResponse:
        async with self._uow:

            mail = await self._mail_gateway.insert(mail=MailDTO(mail=request.mail))

            await self._uow.commit()

        return AddMailResponse(mail=mail)
