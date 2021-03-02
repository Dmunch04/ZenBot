import discord
from discord.ext import commands

from zenbot.bot import ZenBot


class Events(commands.Cog):
    def __init__(self, client: ZenBot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.logger.server('Bot is running! Awaiting user interaction...')

        # Testing of DB
        await self.client.data_manager.db.insert({'id': 'xxyy', 'name': 'Chirp', 'owner': 'yyxx'})
        res = await self.client.data_manager.db.find_by_id('xxyy')
        print(res)
        await self.client.data_manager.db.remove_by_id('xxyy')


def setup(client: commands.Bot):
    client.add_cog(Events(client))
