from typing import NoReturn

from .console_logger import ConsoleLogger
from .file_logger import FileLogger


class LogManager:
    def __init__(self):
        self.console_logger = ConsoleLogger()
        self.file_logger = FileLogger()

    def server(self, msg: str) -> NoReturn:
        self.console_logger.server(msg)

    def debug(self, msg: str) -> NoReturn:
        self.console_logger.debug(msg)

    def error(self, msg: str) -> NoReturn:
        self.console_logger.error(msg)

    def warning(self, msg: str) -> NoReturn:
        self.console_logger.warning(msg)

    def success(self, msg: str) -> NoReturn:
        self.console_logger.success(msg)
