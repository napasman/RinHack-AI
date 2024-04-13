from dataclasses import dataclass

from modules.common.application.dto import MailDTO
from modules.common.application.handlers import Request


@dataclass(frozen=True, kw_only=True)
class AddMailRequest(Request):
    mail: str
