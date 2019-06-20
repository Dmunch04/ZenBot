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
        self.ServerPath = self.Path + 'Server.json'
        self.Config = self.Client.LoadJsonFile (self.ServerPath)

    async def PopulateMembers (self):
        for ServerMember in self.Instance.members:
            MemberToAdd = Member (self.Client, ServerMember, self)

            await self.Members.Add (MemberToAdd)

    async def Set (self, _Type: str, _Sub: str, _Value: str):
        if _Value.lower () in ('true', 'on', 'enable'):
            _Value = True

        elif _Value.lower () in ('false', 'off', 'disable'):
            _Value = False

        if _Type.lower () == 'command':
            for Key in self.Config['Commands']:
                if _Sub.lower () == Key.lower ():
                    self.Config['Commands'][Key] = _Value

                    self.Client.WriteJsonFile (self.ServerPath, self.Config)

        elif _Type.lower () == 'config':
            for Key in self.Config:
                if Key in ('Name', 'Commands', 'ID'):
                    continue

                if _Sub.lower () == Key.lower ():
                    self.Config[Key] = _Value

                    self.Client.WriteJsonFile (self.ServerPath, self.Config)

    async def Get (self, _Type: str, _Sub: str):
        if _Type.lower () == 'command':
            _Type = 'commands'

        for Key in self.Config:
            if _Type.lower () == Key.lower ():
                Object = self.Config.get (Key, None)

                if _Sub:
                    for Sub in self.Config[Key]:
                        if _Sub.lower () == Sub.lower ():
                            if Object:
                                Object = Object.get (Sub, None)

        return Object
