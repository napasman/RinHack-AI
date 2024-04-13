from falcon import HTTP_CREATED
from falcon.asgi import Request, Response

from modules.mail.application import add_mail
from .base import BaseController


class AddMailController(BaseController):
    async def on_post(self, req: Request, resp: Response) -> None:

        handler = await self.provide_dependency(add_mail.AddMailRequestHandler)
        media = await req.get_media()
        request = self._retort.load(media, add_mail.AddMailRequest)

        response = await handler.handle(request)

        resp.media = self._retort.dump(response)
        resp.status = HTTP_CREATED
