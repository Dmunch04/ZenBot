from typing import Dict, Any, NoReturn


class DBObject(object):
    @staticmethod
    def new(*args):
        raise NotImplementedError

    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        raise NotImplementedError

    # TODO: find a better solution for this method signature i guess
    @staticmethod
    def from_dict(data: Dict[str, Any], *, args):
        raise NotImplementedError
