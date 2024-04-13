import datetime
from dataclasses import dataclass, field

from modules.common.domain.timezone import get_current_datetime


@dataclass(frozen=True, kw_only=True)
class MailDTO:
    mail_id: int | None = field(default=None)
    mail: str
    created_at: datetime.datetime = field(default_factory=get_current_datetime)
