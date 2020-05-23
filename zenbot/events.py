import discord
from discord.ext import commands

from zenbot.bot import ZenBot


class Events(commands.Cog):
    def __init__(self, client: ZenBot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.logger.server('Bot is running! Awaiting user interaction...')


def setup(client: commands.Bot):
    client.add_cog(Events(client))
