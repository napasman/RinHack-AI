from dataclasses import dataclass
from typing import Self

from modules.common.application.ports import SourceProviderPort
from modules.common.domain.secrets import SecretsEnum


@dataclass(frozen=True, kw_only=True)
class ApiGatewayConfig:
    api_gateway_base_url: str

    @classmethod
    async def load(cls, source_provider: SourceProviderPort) -> Self:
        return cls(
            api_gateway_base_url=source_provider.get_variable(
                SecretsEnum.API_GATEWAY_BASE_URL, str
            ),
        )
