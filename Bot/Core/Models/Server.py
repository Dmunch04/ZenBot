import json

import discord

from Core.Utilities import Collection
from Core.Models.Plugins import Plugin

class Server:
    def __init__ (self, Client: discord.Client, Server: discord.Guild):
        self.Client = Client
        self.Server = Server

        self.Plugins = Collection (Plugin)
        self.Commands = {}

        Path = f'{self.Client.ServerPath.format (str (self.Server.id))}/Config.json'
        self.Config = self.Client.LoadJsonFile (Path)
