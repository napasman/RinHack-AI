import falcon
from di import Container, ScopeState
from .controllers.base import BaseController


class ContainerMiddleware:
    def __init__(self, container: Container) -> None:
        self._container = container
        self._app_context = None
        self._request_context = None
        self._app_state: ScopeState | None = None
        self._request_state: ScopeState | None = None

    async def process_startup(self, scope, event) -> None:
        self._app_context = self._container.enter_scope("app")
        self._app_state = await self._app_context.__aenter__()

    async def process_shutdown(self, scope, event) -> None:
        await self._app_context.__aexit__(None, None, None)

    async def process_request(self, req: falcon.Request, resp: falcon.Response) -> None:
        self._request_context = self._container.enter_scope(
            "request", state=self._app_state
        )
        self._request_state = await self._request_context.__aenter__()

    async def process_resource(
        self,
        req: falcon.Request,
        resp: falcon.Response,
        resource: BaseController,
        params,
    ) -> None:
        resource.set_request_state(self._request_state)

    async def process_response(
        self,
        req: falcon.Request,
        resp: falcon.Response,
        resource: BaseController,
        req_succeeded: bool,
    ) -> None:
        await self._request_context.__aexit__(None, None, None)
