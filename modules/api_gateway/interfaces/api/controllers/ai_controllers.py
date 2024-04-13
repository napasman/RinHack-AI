from falcon import HTTP_OK
from falcon.asgi import Request, Response

from modules.ai.application import get_ai_results
from .base import BaseController


class GetAIResultsController(BaseController):
    async def on_get(self, req: Request, resp: Response) -> None:

        handler = await self.provide_dependency(
            get_ai_results.GetAIResultsRequestHandler
        )
        request = get_ai_results.GetAIResultsRequest()

        response = await handler.handle(request)

        resp.media = self._retort.dump(response)
        resp.status = HTTP_OK
