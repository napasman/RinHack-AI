import logging.config

from adaptix.load_error import LoadError
from di import Container
from falcon.asgi import App
from modules.api_gateway.interfaces.api import error_handlers
from modules.common.application.errors import ApplicationError
from modules.common.domain.errors import DomainError

from modules.common.main.di import build_container

from .controllers import (
    ai_controllers,
)
from .middlewares import ContainerMiddleware


def build_asgi(container: Container | None = None) -> App:
    logging.config.fileConfig("logging.conf", disable_existing_loggers=False)

    app = App()
    container = container or build_container()

    configure_ai_controllers(app, container)

    app.add_middleware(ContainerMiddleware(container=container))

    return app


def configure_error_handlers(app: App) -> None:
    app.add_error_handler(
        ApplicationError, error_handlers.handle_application_level_error
    )
    app.add_error_handler(DomainError, error_handlers.handle_domain_level_error)
    app.add_error_handler(LoadError, error_handlers.handle_adaptix_load_error)


def configure_ai_controllers(app: App, container: Container) -> None:
    app.add_route(
        "/ai/traffic", ai_controllers.GetAIResultsController(container=container)
    )
