from dataclasses import dataclass

from modules.common.application.dto import MailDTO
from modules.common.application.handlers import Response


@dataclass(frozen=True, kw_only=True)
class AddAIResultResponse(Response):
    mail: MailDTO
