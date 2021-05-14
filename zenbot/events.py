import discord
from discord.ext import commands

from zenbot.bot import ZenBot
from zenbot.models import Server


class Events(commands.Cog):
    def __init__(self, client: ZenBot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.logger.server("Bot is running! Awaiting user interaction...")

    @commands.Cog.listener()
    async def on_guild_join(self, server: discord.Guild):
        # we dont need to do anything here (i think) because adding servers to the cache and db is done in on_message
        pass

    @commands.Cog.listener()
    async def on_guild_remove(self, server: discord.Guild):
        self.client.data_manager.servers.remove(server.id)
        # TODO: should we also remove the server from the DB?

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        # if the server isnt in the cache, put it there
        # NOTE: this also works for newly joined guilds!
        if not self.client.data_manager.servers.has(msg.guild.id):
            server = Server(msg.guild)

            res = await self.client.data_manager.db.find_by_id(msg.guild.id)
            if res:
                server.from_dict(res[0])
            else:
                server.new()
                await self.client.data_manager.db.insert(server.to_dict())

            self.client.data_manager.servers.put(msg.guild.id, server)

        self.client.data_manager.servers.get(msg.guild.id).stats.messages_sent += 1
        # TODO: we need a cache of the servers members. not just a list oof.
        #  how should we do that? like have a function that gets ran by both the `new` and `from_dict` methods

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        self.client.data_manager.servers.get(member.guild.id).stats.current_members += 1

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        self.client.data_manager.servers.get(member.guild.id).stats.current_members -= 1


def setup(client: commands.Bot):
    client.add_cog(Events(client))
