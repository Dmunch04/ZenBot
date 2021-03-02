from ..utils import spacify_string

from typing import (
    Dict,
    Any,
    NoReturn
)


class DBObject(object):
    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        raise NotImplementedError()

    def from_dict(self, data) -> NoReturn:
        for attr in data:
            setattr(self, spacify_string(attr), data[attr])
