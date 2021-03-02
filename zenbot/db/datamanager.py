from .db import Database
from ..utils.collection import Collection
from ..models.server import Server


class DataManager:
    def __init__(self):
        self.db = Database()
        self.servers = Collection(Server)
