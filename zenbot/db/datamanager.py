from .db import Database
from zenbot.utils import Cache
from zenbot.models import Server


class DataManager:
    def __init__(self):
        self.db = Database()
        self.servers = Cache(Server)
