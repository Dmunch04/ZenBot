from typing import List, Any

from zenbot.models import PermissionLevel


class ZenCommandParameter(object):
    __slots__ = ("name", "description", "required", "default")

    def __init__(
        self, name: str, description: str, required: bool = False, default: Any = None
    ):
        self.name = name
        self.description = description
        self.required = required
        self.default = default

    def __str__(self) -> str:
        param_str = ""
        param_str += "<" if self.required else "["
        param_str += self.name
        param_str += f"={str(self.default)}" if self.default else ""
        param_str += ">" if self.required else "]"

        return param_str


class ZenCommand:
    @classmethod
    @property
    def name(cls) -> str:
        raise NotImplementedError

    @classmethod
    @property
    def description(cls) -> str:
        raise NotImplementedError

    @classmethod
    @property
    def category(cls) -> str:
        raise NotImplementedError

    @classmethod
    @property
    def parameters(cls) -> List[ZenCommandParameter]:
        raise NotImplementedError

    @classmethod
    @property
    def example(cls) -> str:
        raise NotImplementedError

    @classmethod
    @property
    def perm_str(cls) -> str:
        raise NotImplementedError

    @classmethod
    @property
    def perm_level(cls) -> PermissionLevel:
        raise NotImplementedError

    @property
    def signature(self) -> str:
        params = [str(param) for param in self.parameters]

        return f"{self.name} {' '.join(params)}"
