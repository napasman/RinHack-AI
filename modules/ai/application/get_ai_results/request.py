from dataclasses import dataclass

from modules.common.application.handlers import Request


@dataclass(frozen=True, kw_only=True)
class GetAIResultsRequest(Request): ...
