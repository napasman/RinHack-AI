import os
from typing import TypeVar

from modules.common.adapters.errors import SourceProviderError
from modules.common.application.ports import SourceProviderPort

T = TypeVar("T")


class EnvSourceProvider(SourceProviderPort):
    def __init__(self) -> None:
        self._source: dict[str, str] = {}

    def get_variable(self, name: str, type_: T = str) -> T:
        try:
            return type_(self._source[name])
        except KeyError as exc:
            raise SourceProviderError(f"Env variable named {name} not found.") from exc

    async def load_source(self) -> None:
        self._source = os.environ
