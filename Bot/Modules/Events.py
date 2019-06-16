from DavesLogger import Logs

import discord
from discord.ext import commands

class Events (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @commands.Cog.listener ()
    async def on_ready (self):
        Logs.Server ('Bot is running! Awaiting user interaction...')

        self.Client.Log ('Bot is running!')

    @commands.Cog.listener ()
    async def on_message (self, _Message: str):
        # Do something here I guess

        await self.Client.process_commands (_Message)

def setup (_Client: discord.Client):
    _Client.add_cog (Events (_Client))
