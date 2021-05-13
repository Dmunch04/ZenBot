from typing import Any, NoReturn


class Cache(dict):
    __slots__ = "instance"

    def __init__(self, instance: Any):
        dict.__init__(self)

        self.instance = instance

    def __iter__(self):
        for value in self.values():
            yield value

    def put(self, key: str, item: Any) -> NoReturn:
        if not isinstance(item, self.instance):
            raise ValueError

        if self.has(key):
            raise ValueError

        self[key] = item

    def get(self, key: str, default: Any = None) -> Any:
        if not self.has(key):
            return default

        return self[key]

    def remove(self, key: str) -> NoReturn:
        if not self.has(key):
            raise ValueError

        del self[key]

    def has(self, key: str) -> bool:
        return key in self
