import os
from typing import AsyncGenerator

from di import Container, bind_by_type
from di.dependent import Dependent
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from modules.common.adapters import persistence
from modules.common.adapters.integration.source_provider.env import EnvSourceProvider
from modules.common.application import ports
from modules.common.main.config import DatabaseConfig, SMTPConfig
from dotenv import load_dotenv

from modules.mail.adapters.integration import SMTP
from modules.mail.application.common.ports import SMTPPort

load_dotenv()


def build_container() -> Container:
    container = Container()

    container.bind(
        bind_by_type(
            Dependent(provide_source_provider, scope="app"), ports.SourceProviderPort
        )
    )
    container.bind(
        bind_by_type(Dependent(DatabaseConfig.load, scope="app"), DatabaseConfig)
    )
    container.bind(bind_by_type(Dependent(SMTPConfig.load, scope="app"), SMTPConfig))
    container.bind(
        bind_by_type(Dependent(persistence.UoW, scope="request"), ports.UoWPort)
    )
    container.bind(
        bind_by_type(
            Dependent(persistence.AIGateway, scope="request"), ports.AIGatewayPort
        )
    )
    container.bind(
        bind_by_type(
            Dependent(persistence.MailGateway, scope="request"), ports.MailGatewayPort
        )
    )
    container.bind(
        bind_by_type(
            Dependent(SMTP, scope="request"), SMTPPort
        )
    )
    container.bind(
        bind_by_type(Dependent(provide_sqlalchemy_engine, scope="request"), AsyncEngine)
    )
    container.bind(
        bind_by_type(
            Dependent(provide_sqlalchemy_sessionmaker, scope="request"),
            async_sessionmaker[AsyncSession],
        )
    )
    container.bind(
        bind_by_type(
            Dependent(provide_sqlachemy_session, scope="request"),
            AsyncSession,
        )
    )

    return container


def provide_sqlalchemy_engine(config: DatabaseConfig) -> AsyncEngine:
    return create_async_engine(config.connection_string, echo=True, pool_pre_ping=True)


def provide_sqlalchemy_sessionmaker(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine)


async def provide_sqlachemy_session(
    sessionmaker: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    async with sessionmaker() as session:
        yield session


async def provide_source_provider() -> ports.SourceProviderPort:
    source_provider_name = os.getenv("SOURCE_PROVIDER")
    print("СОУРС ПРОВАЙДЕР", source_provider_name)
    if source_provider_name == "env":
        source_provider = EnvSourceProvider()
    else:
        raise RuntimeError("Wrong source provider!")

    await source_provider.load_source()

    return source_provider
