import json
import logging
import datetime

import discord
from discord.ext import commands

from Core import PluginDatabase, Database

Log = logging.getLogger (__name__)

class ZenBot (commands.Bot):
    def __init__ (self):
        super ().__init__ (
            command_prefix = self.Prefix,
            description = self.Description,
            activity = discord.Game (name = self.Status.format (self.Prefix)),
            case_insensitive = True,
            max_messages = 10_000
        )

        # Setup the bot's database
        self.Database = Database (self)
        self.Database.PluginDatabase = PluginDatabase (self)

    @property
    def Config (self) -> str:
        with open ('Data/Config.json', 'r') as Config:
            return json.loads (Config.read ())

    @property
    def DataPath (self) -> str:
        return self.Config.get ('DataPath', 'Data')

    @property
    def Prefix (self) -> str:
        return self.Config.get ('Prefix', '!')

    @property
    def Description (self) -> str:
        return self.Config.get ('Description', 'The official ZenBot')

    @property
    def Status (self) -> str:
        return self.Config.get ('Status', 'Help - {}help')

    async def IsOwner (self, _User: discord.User) -> bool:
        Raw = str (self.Config.get ('Owners', '0')).split (',')
        Allowed = { int (I) for I in Raw }

        return (_User.id in Allowed) or await super ().is_owner (_User)

    def LoadJsonFile (self, _Path: str) -> dict:
        with open (_Path, 'r') as File:
            Data = json.loads (File.read ())

        return Data

    def Log (self, _Text: str):
        with open ('Data/Log.txt', 'a') as Log:
            Text = str (_Text) + '\n'

            Log.write (Text)

    def LoadExtensions (self, _Folder: str = '', _Extensions: list = [], _Suffix: str = ''):
        for Extension in _Extensions:
            Name = Extension
            Extension = '{0}.{1}{2}'.format (_Folder, Extension, _Suffix)

            try:
                self.load_extension (Extension)

                Name = str (Name.split ('.')[-1])
                self.Log (f'- {Name} was successfully loaded!')

            except Exception as Error:
                ErrorMessage = '{0} cannot be loaded. Error: {1}'.format (Extension, Error)
                print (ErrorMessage)

                self.Log (f'- {ErrorMessage}')

    def Run (self):
        self.Log ('--------------------')
        self.Log (f'Bot started at: {str (datetime.datetime.now ())}')

        self.remove_command ('help')
        self.Log ('Removed help command!\n')

        self.Log ('Loading commands...')
        Errors = self.LoadExtensions ('Commands', self.Config.get ('Commands', []), 'Command')
        self.Log ('\n')

        self.Log ('Loading Modules...')
        self.LoadExtensions ('Modules', self.Config.get ('Modules', []))
        self.Log ('\n')

        self.Log ('Running bot...')
        self.run (self.Config.get ('Token', ''))
