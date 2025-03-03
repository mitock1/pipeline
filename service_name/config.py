"""Module for defining the configs for different environments."""
import os
from functools import lru_cache


# config settings, do not add plain text credentials
# or your personal machine settings here, please use encrypted values

ENCRYPTED_VALUES = [
    "SQLALCHEMY_DATABASE_URI",
]

APP_NAME = os.getenv("APP_NAME", "service_name")
DATABASE_SCHEMA = "service_name"
INIT_DATA_PATH = "init_data"
dir_path = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    """Base configuration."""

    APP_NAME = APP_NAME
    DATABASE_SCHEMA = DATABASE_SCHEMA
    INIT_DATA_PATH = INIT_DATA_PATH

    ENV = "development"
    LOG_LEVEL = "DEBUG" if os.getenv("DEBUG") else "INFO"
    LOG_NAME = "service_name.log"
    LOG_INCLUDE_STREAM_HANDLER = True
    LOG_INCLUDE_FILE_HANDLER = False
    LOG_INCLUDE_SPLUNK_HANDLER = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 10,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
    }
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        r"mssql+pyodbc://USER:PASSWORD@127.0.0.1:1433/TABLE",
    )

    OPENAPI_PREFIX = ""


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    SQLALCHEMY_DATABASE_URI = ""
    DEBUG = True
    LOG_INCLUDE_STREAM_HANDLER = False
    LOG_INCLUDE_SPLUNK_HANDLER = True

    OPENAPI_PREFIX = ""


class StagingConfig(BaseConfig):
    """Staging configuration."""

    ENV = "staging"
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = ""
    LOG_INCLUDE_STREAM_HANDLER = False
    LOG_INCLUDE_SPLUNK_HANDLER = True

    OPENAPI_PREFIX = ""


class UatConfig(BaseConfig):
    """Uat configuration."""

    ENV = "uat"
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = ""

    LOG_INCLUDE_STREAM_HANDLER = False
    LOG_INCLUDE_SPLUNK_HANDLER = True

    OPENAPI_PREFIX = ""


class ProductionConfig(BaseConfig):
    """Production configuration."""

    ENV = "production"
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = ""
    LOG_INCLUDE_STREAM_HANDLER = False
    LOG_INCLUDE_SPLUNK_HANDLER = True

    OPENAPI_PREFIX = ""


class TestingConfig(BaseConfig):
    """Testing configuration. Used for pytests"""

    ENV = "test"
    LOG_INCLUDE_STREAM_HANDLER = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_TEST_URL",
        r"mssql+pyodbc://USER:PASSWORD@127.0.0.1:1433/TABLE",
    )


@lru_cache()
def get_config(config=BaseConfig) -> BaseConfig:
    return config


def get_env_name():
    config = get_config()

    if config.ENV == "production":
        return "prod"

    if config.ENV == "development":
        return "dev"

    return config.ENV


def environment_is_develop():
    config = get_config()
    return config.ENV == "dev"
