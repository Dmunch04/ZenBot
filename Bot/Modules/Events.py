import aiohttp

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

        # Makes commands run twice
        #await self.Client.process_commands (_Message)

        pass

    @commands.Cog.listener ()
    async def on_error (self, _Error: str):
        Logs.Error (_Error)

    @commands.Cog.listener ()
    async def on_guild_join (self, _Server: discord.Guild):
        # Update the clients database for this server for it's servers
        # And create a data folder and data files for it
        # Send request to discordbots.org API to update the stats

        Name = _Server.name
        Id = _Server.id

        TotalChannels = len (_Server.channels)
        TotalRoles = len (_Server.roles)
        TotalMembers = _Server.member_count

        Owner = str (_Server.owner)
        CreatedAt = _Server.created_at.strftime("%A, %d %B %Y, %H:%M")

        Icon = str (_Server.icon_url)
        if Icon == '':
            Icon = 'https://cdn-images-1.medium.com/max/1600/0*FDdiWdrriXPKGNyf.png'
        
        WebhookData = self.Client.LoadJsonFile ('Data/Config.json')
        Url = WebhookData['Webhook']

        Data = {}
        Data['embeds'] = [
        {
            'title' : 'Server Joined',
            'description' : f'{self.Client.user.name} Joined a Server',
            'color' : 0x00FF00,
            
            'thumbnail' : {
                'url' : Icon
            },
            'footer' : {
                'text' : f'Currently in {len (self.Client.guilds)} Servers'
            },

            'fields' : [
                {
                    'name' : 'Server Name',
                    'value' : Name,
                    'inline' : True
                },
                {
                    'name' : 'Server ID',
                    'value' : Id,
                    'inline' : True
                },
                {
                    'name' : 'Server Owner',
                    'value' : Owner,
                    'inline' : True
                },
                {
                    'name' : 'Total Members',
                    'value' : TotalMembers,
                    'inline' : True
                },
                {
                    'name' : 'Total Channels',
                    'value' : TotalChannels,
                    'inline' : True
                },
                {
                    'name' : 'Total Roles',
                    'value' : TotalRoles,
                    'inline' : True
                },
                {
                    'name' : 'Server Created At',
                    'value' : CreatedAt,
                    'inline' : True
                },
            ]
        }
        ]
        
        async with aiohttp.ClientSession () as Session:
            await Session.post (url=Url, json=Data)

    @commands.Cog.listener ()
    async def on_guild_remove (self, _Server: discord.Guild):
        # Update the clients database for this server for it's servers
        # And create a data folder and data files for it
        # Send request to discordbots.org API to update the stats

        Name = _Server.name
        Id = _Server.id

        TotalChannels = len (_Server.channels)
        TotalRoles = len (_Server.roles)
        TotalMembers = _Server.member_count

        Owner = str (_Server.owner)
        CreatedAt = _Server.created_at.strftime("%A, %d %B %Y, %H:%M")

        Icon = str (_Server.icon_url)
        if Icon == '':
            Icon = 'https://cdn-images-1.medium.com/max/1600/0*FDdiWdrriXPKGNyf.png'
        
        WebhookData = self.Client.LoadJsonFile ('Data/Config.json')
        Url = WebhookData['Webhook']

        Data = {}
        Data['embeds'] = [
        {
            'title' : 'Server Left',
            'description' : f'{self.Client.user.name} Left a Server',
            'color' : 0xff0000,
            
            'thumbnail' : {
                'url' : Icon
            },
            'footer' : {
                'text' : f'Currently in {len (self.Client.guilds)} Servers'
            },

            'fields' : [
                {
                    'name' : 'Server Name',
                    'value' : Name,
                    'inline' : True
                },
                {
                    'name' : 'Server ID',
                    'value' : Id,
                    'inline' : True
                },
                {
                    'name' : 'Server Owner',
                    'value' : Owner,
                    'inline' : True
                },
                {
                    'name' : 'Total Members',
                    'value' : TotalMembers,
                    'inline' : True
                },
                {
                    'name' : 'Total Channels',
                    'value' : TotalChannels,
                    'inline' : True
                },
                {
                    'name' : 'Total Roles',
                    'value' : TotalRoles,
                    'inline' : True
                },
                {
                    'name' : 'Server Created At',
                    'value' : CreatedAt,
                    'inline' : True
                },
            ]
        }
        ]
        
        async with aiohttp.ClientSession () as Session:
            await Session.post (url=Url, json=Data)

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
