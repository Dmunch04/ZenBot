import json

import discord

from Core.Plugins import Plugin
from Utilities import Collection

class Server:
    async def __init__ (self, Client: discord.Client, Server: discord.Guild):
        self.Client = Client
        self.Server = Server

        self.Plugins = Collection (Plugin)
        self.Commands = {}

        Path = f'{self.Client.ServerPath.format (str (self.Server.id))}/Config.json'
        self.Config = await self.Client.LoadJsonFile (Path)
