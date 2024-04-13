import logging

from adaptix.load_error import LoadError
from falcon import Request, Response, status_codes
from modules.common.application.errors import ApplicationError
from modules.common.domain.errors import DomainError

logger = logging.getLogger(__name__)


async def handle_application_level_error(
    req: Request, resp: Response, error: ApplicationError, params: dict
) -> None:
    resp.media = {
        "type": "ApplicationError",
        "subtype": type(error).__name__,
        "message": str(error),
    }
    resp.status = status_codes.HTTP_BAD_REQUEST


async def handle_domain_level_error(
    req: Request, resp: Response, error: DomainError, params: dict
) -> None:
    resp.media = {
        "type": "DomainError",
        "subtype": type(error).__name__,
        "message": str(error),
    }
    resp.status = status_codes.HTTP_CONFLICT


async def handle_adaptix_load_error(
    req: Request, resp: Response, error: LoadError, params: dict
) -> None:
    resp.media = {
        "type": "LoadError",
        "subtype": type(error).__name__,
        "message": "Unprocessable entity",
    }
    resp.status = status_codes.HTTP_UNPROCESSABLE_ENTITY
