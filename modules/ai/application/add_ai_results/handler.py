from modules.common.application import ports
from modules.common.application.handlers import RequestHandler
from modules.mail.application.common.ports import SMTPPort

from .request import AddAIResultRequest
from .response import AddAIResultResponse


class AddAIResultsRequestHandler(
    RequestHandler[AddAIResultRequest, AddAIResultResponse]
):
    def __init__(
        self,
        ai_gateway: ports.AIGatewayPort,
        mail_gateway: ports.MailGatewayPort,
        smtp: SMTPPort,
        uow: ports.UoWPort,
    ) -> None:
        self._ai_gateway = ai_gateway
        self._mail_gateway = mail_gateway
        self._smtp = smtp
        self._uow = uow

    async def handle(self, request: AddAIResultRequest) -> AddAIResultResponse:
        async with self._uow:
            traffic_list = await self._ai_gateway.insert_bulk(
                traffic_list=request.traffic
            )

            mails = await self._mail_gateway.get_mails()

            mails_list = [mail.mail for mail in mails]

            for traffic in traffic_list:
                if traffic.flag == "true":
                    smtp_message = f"Объект под id {traffic.id} является угрозой\n\n{traffic.__dict__}"
                    await self._smtp.send_messages(mails=mails_list, msg_text=smtp_message)

            await self._uow.commit()

        return AddAIResultResponse(traffic=traffic_list)
