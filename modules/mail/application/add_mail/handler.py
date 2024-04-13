from modules.common.application import ports
from modules.common.application.handlers import RequestHandler

from .request import AddAIResultRequest
from .response import AddAIResultResponse


class AddAIResultsRequestHandler(
    RequestHandler[AddAIResultRequest, AddAIResultResponse]
):
    def __init__(
        self,
        ai_gateway: ports.AIGatewayPort,
        uow: ports.UoWPort,
    ) -> None:
        self._ai_gateway = ai_gateway
        self._uow = uow

    async def handle(self, request: AddAIResultRequest) -> AddAIResultResponse:
        async with self._uow:
            traffic = await self._ai_gateway.insert(traffic=request.traffic)

        return AddAIResultResponse(traffic=traffic)
