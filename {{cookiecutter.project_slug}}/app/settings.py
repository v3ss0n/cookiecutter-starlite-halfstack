"""All configuration via environment.

Take note of the environment variable prefixes required for each
settings class, except `AppSettings`.
"""
from typing import Literal

from pydantic import AnyUrl, BaseSettings, PostgresDsn


# noinspection PyUnresolvedReferences


# noinspection PyUnresolvedReferences
class ServerSettings(BaseSettings):
    class Config:
        env_prefix = "UVICORN_"
        case_sensitive = True

    HOST: str
    LOG_LEVEL: str
    PORT: int
    RELOAD: bool
    KEEPALIVE: int


class EmailSettings(BaseSettings):
    class Config:
        env_prefix = "EMAIL_"
        case_sensitive = True

    HOST: str
    NEW_AUTHOR_SUBJECT: str
    PORT: int
    RECIPIENT: str
    SENDER: str


# `.parse_obj()` thing is a workaround for pyright and pydantic interplay, see:
# https://github.com/pydantic/pydantic/issues/3753#issuecomment-1087417884

email = EmailSettings.parse_obj({})
server = ServerSettings.parse_obj({})
