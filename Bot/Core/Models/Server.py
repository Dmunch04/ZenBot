import json

import discord

from Core.Models.Member import Member
from Core.Utilities import Collection
from Core.Models.Plugins import Plugin

class Server:
    def __init__ (self, Client: discord.Client, Server: discord.Guild):
        self.Client = Client
        self.Instance = Server
        self.ID = Server.id

        self.Plugins = Collection (Plugin)
        self.Commands = {}

        self.Members = Collection (Member)

        self.Path = f'{self.Client.ServerPath.format (str (self.Instance.id))}/'
        ServerPath = self.Path + 'Server.json'
        #self.Config = self.Client.LoadJsonFile (ServerPath)

    async def PopulateMembers (self):
        for ServerMember in self.Instance.members:
            MemberToAdd = Member (self.Client, ServerMember, self)

            await self.Members.Add (MemberToAdd)
