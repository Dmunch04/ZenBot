from typing import NoReturn

from DavesLogger import Logs

from .logger import Logger


class ConsoleLogger(Logger):
    def server(self, msg: str) -> NoReturn:
        Logs.Server(msg)

    def debug(self, msg: str) -> NoReturn:
        Logs.Debug(msg)

    def error(self, msg: str) -> NoReturn:
        Logs.Error(msg)

    def warning(self, msg: str) -> NoReturn:
        Logs.Warning(msg)

    def success(self, msg: str) -> NoReturn:
        Logs.Success(msg)
