"""Logging stuff"""
import sys
from logging import FileHandler
from logging import Formatter
from logging import getLogger
from logging import StreamHandler

from .config import get_config

config = get_config()

# A simple logger


def get_logger(log_name: str):
    stream = sys.stdout
    _logger = getLogger(log_name)
    formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    if config.LOG_INCLUDE_STREAM_HANDLER:
        stream_handler = StreamHandler(stream=stream)
        stream_handler.setLevel(level=config.LOG_LEVEL)
        stream_handler.setFormatter(formatter)
        _logger.addHandler(stream_handler)
    if config.LOG_INCLUDE_FILE_HANDLER:
        file_handler = FileHandler(config.LOG_NAME, mode="a", encoding="utf-8")
        file_handler.setLevel(level=config.LOG_LEVEL)
        file_handler.setFormatter(formatter)
        _logger.addHandler(file_handler)

    return _logger


logger = get_logger(config.LOG_NAME)
