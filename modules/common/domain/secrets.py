from enum import auto

from .enums import UpperStrEnum


class SecretsEnum(UpperStrEnum):
    DATABASE_CONNECTION_STRING = auto()
    API_GATEWAY_BASE_URL = auto()
