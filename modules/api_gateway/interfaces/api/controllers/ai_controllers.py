from falcon import HTTP_OK, HTTP_CREATED
from falcon.asgi import Request, Response

from modules.ai.application import get_ai_results, add_ai_results
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


class AddAIResultsController(BaseController):
    async def on_post(self, req: Request, resp: Response) -> None:

        handler = await self.provide_dependency(
            add_ai_results.AddAIResultsRequestHandler
        )
        media = await req.get_media()
        request = self._retort.load(media, add_ai_results.AddAIResultRequest)

        response = await handler.handle(request)

        resp.media = self._retort.dump(response)
        resp.status = HTTP_CREATED
