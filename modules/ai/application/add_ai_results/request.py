from dataclasses import dataclass

from modules.common.application.dto import TrafficDTO
from modules.common.application.handlers import Request


@dataclass(frozen=True, kw_only=True)
class AddAIResultRequest(Request):
    traffic: list[TrafficDTO]
