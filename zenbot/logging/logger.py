from typing import (
    NoReturn
)


class Logger:
    def server(self, msg: str) -> NoReturn: raise NotImplementedError()
    def debug(self, msg: str) -> NoReturn: raise NotImplementedError()
    def error(self, msg: str) -> NoReturn: raise NotImplementedError()
    def warning(self, msg: str) -> NoReturn: raise NotImplementedError()
    def success(self, msg: str) -> NoReturn: raise NotImplementedError()
