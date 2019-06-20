import discord

from Core.Models import Server
from Core.Utilities import Collection

class Database:
    def __init__ (self, Client: discord.Client):
        self.Client = Client

        self.Servers = Collection (Server)

        self.PluginRegestry = None
        self.Client.loop.create_task (self.PopulatePluginRegestry ())

    async def PopulateDatabase (self):
        for BotServer in self.Client.guilds:
            ServerToAdd = Server (self.Client, BotServer)
            await ServerToAdd.PopulateMembers ()

            await self.Servers.Add (ServerToAdd)

    async def PopulatePluginRegestry (self):
        Path = self.Client.DataPath + '/Plugins.json'

        Plugins = self.Client.LoadJsonFile (Path)

        self.PluginRegestry = Plugins

    async def GetServer (self, _ID: int) -> Server:
        Server = await self.Servers.Get (_ID)

        return Server
