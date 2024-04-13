from typing import Protocol, Type, TypeVar

T = TypeVar("T")


class SourceProviderPort(Protocol):
    def get_variable(self, name: str, type_: Type[T]) -> T:
        raise NotImplementedError

    async def load_source(self) -> None:
        raise NotImplementedError
