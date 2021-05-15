import discord
from discord.ext import commands

from zenbot.models import Server
from zenbot.utils import Cache
from .db import Database


class DataManager:
    def __init__(self):
        self.db = Database()
        self.servers = Cache(Server)

    async def update_server_cache(self, bot: commands.Bot, server: discord.Guild):
        if not self.servers.has(server.id):
            res = await self.db.find_by_id(server.id)
            if res:
                server = Server.from_dict(res[0], server)
                await server.update_members_cache(server)
            else:
                server = Server.new(bot, server)
                #await self.db.insert(server.to_dict())
                # TODO: this isnt an optimal solution to the problem, but it works for now
                await self.db.update_by_id(server.id, server.to_dict())

            self.servers.put(server.id, server, silent=True)

    async def save_cache_to_db(self):
        for server in self.servers:
            await self.db.update_by_id(server.id, server.to_dict())
