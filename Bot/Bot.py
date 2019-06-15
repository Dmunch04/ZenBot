import logging

import discord
from discord.ext import commands

from Core import PluginDatabase

Log = logging.getLogger (__name__)

class ZenBot (commands.Bot):
    def __init__ (self):
        with open ('Data/Config.json', 'r') as Config:
            self.Config = json.loads (Config.read ())

        self.Prefix = self.Config.get ('Prefix', '!')
        self.Description = self.Config.get ('Description', 'The official ZenBot')
        self.Status = self.Config.get ('Status', 'Help - {}help')

        super ().__init__ (
            command_prefix = self.Prefix,
            description = self.Description,
            activity = discord.Game (name = self.Status.format (self.Prefix)),
            case_insensitive = True,
            max_messages = 10_000
        )

        self.PluginDatabase = PluginDatabase (self)

    @property
    def Prefix (self) -> str:
        return self.Config.get ('Prefix', '!')

    async def IsOwner (self, _User: discord.User) -> bool:
        Raw = str (self.Config.get ('Owners', '0')).split (',')
        Allowed = { int (I) for I in Raw }

        return (_User.id in Allowed) or await super ().is_owner (_User)

    async def LoadExtensions (self, _Folder: str = '', _Extensions: list, _Suffix: str = ''):
        for Extension in _Extensions:
            Extension = '{0}.{1}{2}'.format (_Folder, Extension, _Suffix)

            try:
                self.load_extension (Extension)

            except Exception as Error:
                ErrorMessage = '{0} cannot be loaded. Error: {1}'.format (Extension, Error)
                print (ErrorMessage)

    async def Run (self):
        self.remove_command ('help')

        await self.LoadCogs ('Commands', self.Config.get ('Commands', []), 'Commands')
        await self.LoadCogs ('Modules', self.Config.get ('Modules', []))

        self.run (self.Config.get ('Token', ''))
