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

        # Populate the database
        await self.Client.Database.PopulateDatabase ()

    @commands.Cog.listener ()
    async def on_message (self, _Message: str):
        # Do something here I guess

        await self.Client.process_commands (_Message)

    @commands.Cog.listener ()
    async def on_error (self, _Error: str):
        Logs.Error (_Error)

    @commands.Cog.listener ()
    async def on_guild_join (self, _Server: discord.Guild):
        # Update the clients database for this server for it's servers
        # And create a data folder and data files for it

        pass

    @commands.Cog.listener ()
    async def on_guild_remove (self, _Server: discord.Guild):
        # Update the clients database for this server for it's servers
        # And create a data folder and data files for it

        pass

    @commands.Cog.listener ()
    async def on_guild_channel_create (self, _Channel: discord.abc.GuildChannel):
        Server = _Channel.guild

        # Update the clients database for this server for it's channels

    @commands.Cog.listener ()
    async def on_guild_channel_delete (self, _Channel: discord.abc.GuildChannel):
        Server = _Channel.guild

        # Update the clients database for this server for it's channels

    @commands.Cog.listener ()
    async def on_member_join (self, _Member: discord.Member):
        Server = _Member.guild

        # Update the clients database for this server for it's members
        # And create a data folder and files for this user

    @commands.Cog.listener ()
    async def on_member_remove (self, _Member: discord.Member):
        Server = _Member.guild

        # Update the clients database for this server for it's members
        # And delete the users data folder in the servers data folder

def setup (_Client: discord.Client):
    _Client.add_cog (Events (_Client))
