from .db import Database
from zenbot.utils import Cache
from zenbot.models import Server


class DataManager:
    def __init__(self):
        self.db = Database()
        self.servers = Cache(Server)

    async def save_cache_to_db(self):
        for server in self.servers:
            await self.db.update_by_id(server.id, server.to_dict())
