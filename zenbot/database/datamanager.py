from .db import Database
from ..utils.collection import Collection
from ..models.server import Server

from typing import (
    Dict
)


class DataManager:
    def __init__(self, config: Dict[str, str]):
        self.db = Database(config)
        self.servers = Collection(Server)
