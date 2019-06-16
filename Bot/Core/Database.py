import discord

from Core import Server

class Database:
    def __init__ (self, Client):
        self.Client = Client

        self.PluginDatabase = None
        self.PopulatePluginDatabase ()

    def PopulatePluginDatabase (self):
        Path = self.Client.DataPath + '/Plugins.json'

        Plugins = self.Client.LoadJsonFile (Path)

        self.PluginDatabase = Plugins

    async def GetServer (self, _ID: int):
        Server = self.Client.get_guild (_ID)

        return Server (Server, self)
