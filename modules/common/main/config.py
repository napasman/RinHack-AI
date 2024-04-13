from dataclasses import dataclass
from typing import Self

from modules.common.application.ports import SourceProviderPort
from modules.common.domain.secrets import SecretsEnum


@dataclass(frozen=True, kw_only=True)
class DatabaseConfig:
    connection_string: str

    @classmethod
    async def load(cls, source_provider: SourceProviderPort) -> Self:
        return cls(
            connection_string=source_provider.get_variable(
                SecretsEnum.DATABASE_CONNECTION_STRING, str
            )
        )


@dataclass(frozen=True, kw_only=True)
class SMTPConfig:
    login: str
    password: str

    @classmethod
    async def load(cls, source_provider: SourceProviderPort) -> Self:
        return cls(
            login=source_provider.get_variable(SecretsEnum.SMTP_LOGIN, str),
            password=source_provider.get_variable(SecretsEnum.SMTP_PASSWORD, str),
        )
