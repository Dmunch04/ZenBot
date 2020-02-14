from DavesLogger import Logs

import discord
from discord.ext import commands

class Events (commands.Cog):
    def __init__ (self, Client: commands.Bot):
        self.Client = Client

    @commands.Cog.listener ()
    async def on_ready (self):
        Logs.Server ('Bot is running! Awaiting user interaction...')

    @commands.Cog.listener ()
    async def on_error (self):
        Logs.Error ('Yeet')

def setup (Client: commands.Bot):
    Client.add_cog (Events (Client))