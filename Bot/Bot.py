# Module imports
import json
import logging
import datetime
from DavesLogger import Logs

# Discord imports
import discord
from discord.ext import commands

# File/Function imports
from Core import PluginDatabase, Database, PermissionLevel

Log = logging.getLogger ('ZenBot')

class ZenBot (commands.Bot):
    """ Main bot class. This will be the core of our bot """

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

        self.Website = 'http://zenbot.xyz/'

    @property
    def Config (self) -> str:
        with open ('Data/Config.json', 'r') as Config:
            return json.loads (Config.read ())

    @property
    def DataPath (self) -> str:
        return self.Config.get ('DataPath', 'Data')

    @property
    def ServerPath (self) -> str:
        return self.DataPath + '/Servers/{}'

    @property
    def Prefix (self) -> str:
        return self.Config.get ('Prefix', '!')

    @property
    def Description (self) -> str:
        return self.Config.get ('Description', 'The official ZenBot')

    @property
    def Status (self) -> str:
        return self.Config.get ('Status', 'Help - {}help')

    def LoadJsonFile (self, _Path: str) -> dict:
        """ Loads a JSON file, and returns it's content """

        with open (_Path, 'r') as File:
            Data = json.loads (File.read ())

        return Data

    def WriteJsonFile (self, _Path: str, _Data: dict) -> None:
        """ Writes a dict of data to a file """

        with open (_Path, 'w+') as File:
            File.write (json.dumps (_Data))

    def Log (self, _Text: str):
        """ Writes text to the Logs file """

        with open ('Data/Log.txt', 'a') as Log:
            Text = str (_Text) + '\n'

            Log.write (Text)

    def LoadExtensions (self, _Folder: str = '', _Extensions: list = [], _Suffix: str = ''):
        """ Loads a list of extensions """

        for Extension in _Extensions:
            Name = Extension.split ('.')[-1]
            Extension = f'{_Folder}.{Extension}{_Suffix}'

            try:
                self.load_extension (Extension)

                self.Log (f'- {Name} was successfully loaded!')

            except Exception as Error:
                ErrorMessage = f'{Name} cannot be loaded. Error: {Error}'
                Logs.Error (ErrorMessage)

                self.Log (f'- {ErrorMessage}')

    def Run (self):
        """ Run & Prepare the bot. And add some logs to the Logs file """

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
        self.Log ('\n')

        self.run (self.Config.get ('Token', ''))
