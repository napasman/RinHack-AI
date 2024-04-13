from typing import Type, TypeVar

from adaptix import Retort
from di import Container, ScopeState
from di.dependent import Dependent
from di.executors import AsyncExecutor
from falcon import Request

T = TypeVar("T")


class BaseController:
    def __init__(self, container: Container) -> None:
        self._container = container
        self._retort = Retort()
        self._executor = AsyncExecutor()
        self._request_state: ScopeState | None = None

    def set_request_state(self, state: ScopeState) -> None:
        self._request_state = state

    async def provide_dependency(self, type_: Type[T]) -> T:
        solved = self._container.solve(
            Dependent(type_, scope="request"), scopes=["app", "request"]
        )
        return await solved.execute_async(
            executor=self._executor, state=self._request_state
        )
