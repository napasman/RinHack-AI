from modules.common.application import ports
from modules.common.application.handlers import RequestHandler

from .request import GetAIResultsRequest
from .response import GetAIResultsResponse


class GetAIResultsRequestHandler(
    RequestHandler[GetAIResultsRequest, GetAIResultsResponse]
):
    def __init__(
        self,
        ai_gateway: ports.AIGatewayPort,
        uow: ports.UoWPort,
    ) -> None:
        self._ai_gateway = ai_gateway
        self._uow = uow

    async def handle(self, request: GetAIResultsRequest) -> GetAIResultsResponse:
        async with self._uow:
            traffic = await self._ai_gateway.get_ai_results()

        return GetAIResultsResponse(traffic=traffic)
