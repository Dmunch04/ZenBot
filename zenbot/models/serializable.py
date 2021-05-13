from typing import Dict, Any, NoReturn


class DBObject(object):
    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> NoReturn:
        raise NotImplementedError
