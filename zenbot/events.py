import discord
from discord.ext import commands

from zenbot.models import Server


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.logger.server("Bot is running! Awaiting user interaction...")

    @commands.Cog.listener()
    async def on_guild_join(self, server: discord.Guild):
        # we dont need to do anything here (i think) because adding servers to the cache and db is done in on_message
        pass

    @commands.Cog.listener()
    async def on_guild_remove(self, server: discord.Guild):
        self.bot.data_manager.servers.remove(server.id)
        # TODO: should we also remove the server from the DB?

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        # if the server isnt in the cache, put it there
        # NOTE: this also works for newly joined guilds!
        if not self.bot.data_manager.servers.has(msg.guild.id):
            res = await self.bot.data_manager.db.find_by_id(msg.guild.id)
            if res:
                server = Server.from_dict(res[0], msg.guild)
            else:
                server = Server.new(msg.guild)
                await self.bot.data_manager.db.insert(server.to_dict())

            self.bot.data_manager.servers.put(msg.guild.id, server)

        self.bot.data_manager.servers.get(msg.guild.id).stats.messages_sent += 1
        self.bot.data_manager.servers.get(msg.guild.id).members.get(
            msg.author.id
        ).messages_sent += 1

        #! ONLY FOR TESTING
        await self.bot.data_manager.save_cache_to_db()

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        self.bot.data_manager.servers.get(member.guild.id).stats.current_members += 1

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        self.bot.data_manager.servers.get(member.guild.id).stats.current_members -= 1


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
