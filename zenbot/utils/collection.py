from typing import (
    Any,
    NoReturn,
    List,
    Callable
)


class Collection(dict):
    __slots__ = ('data', 'index', 'instance')

    def __init__(self, instance: Any = dict, indexor: str = "id"):
        dict.__init__(self)
        self.index = indexor
        self.instance = instance

    def __iter__(self):
        for value in self.values():
            yield value

    def __add__(self, other):
        if isinstance(other, Collection):
            if isinstance(other.instance, self.instance):
                [self.add(item) for item in other]
        elif isinstance(other, self.instance):
            self.add(other)
        else:
            raise ValueError('Item is not collection or instance of!')

    def __iadd__(self, other):
        self.__add__(other)

    def __setitem__(self, key, value):
        if not isinstance(value, self.instance):
            raise ValueError(f'{value} is not an instance of {self.instance}!')
        dict.__setitem__(self, key, value)

    def add(self, item: Any) -> NoReturn:
        if not isinstance(item, self.instance):
            raise ValueError(f'{item} is not an instance of {self.instance}!')
        index = getattr(item, self.index, None)
        if index is None:
            raise AttributeError(f'{self.index} of {repr(item)} is invalid!')
        self[index] = item

    def remove(self, item: Any) -> NoReturn:
        if isinstance(item, self.instance):
            if getattr(item, self.index, None) is not None:
                del self[getattr(item, self.index)]
        else:
            if item in self:
                del self[item]

    def remove_if(self, **attrs: dict) -> NoReturn:
        for key, value in reversed(self.items()):
            if self.has_attrs(value, attrs):
                del self[key]

    def has_attrs(self, obj: Any, **attrs: dict) -> bool:
        for key, value in attrs.items():
            if not getattr(obj, key, None) == value:
                return False
        return True

    def has(self, key: Any) -> bool:
        if isinstance(key, self.instance):
            return self.__contains__(key)
        for item in self:
            if getattr(item, self.index, None) == key:
                return True
        return False

    def find(self, cond: Callable) -> List[Any]:
        return [item for item in self if cond(item)]

    def find_one(self, cond: Callable) -> Any:
        for item in self:
            if cond(item):
                return item

    def get(self, id: Any = None, **attrs: dict):
        attrs['id'] = id or attrs.get('id')
        return self.find_one(lambda i: self.has_attrs(i, **attrs))
