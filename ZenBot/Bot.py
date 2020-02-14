import json
from datetime import datetime

from DavesLogger import Logs

import discord
from discord.ext import commands

from Database.DatabaseHandler import Database
from Core.Utils import Helper


class ZenBot (commands.Bot):
    def __init__ (self):
        super ().__init__ (
            command_prefix = Helper.GetPrefix,
            description = self.Description,
            activity = discord.Game (name = self.Status.format (Helper.GetPrefix)), # TODO: Fix so it displays the server's specified prefix
            case_insensitive = True,
            max_messages = 10_000
        )

        self.Website = 'http://zenbot.xyz'
        self.Plugins = []

        self.Database = Database (
            self.DBConfig.get ('Host'),
            self.DBConfig.get ('Port'),
            self.DBConfig.get ('DatabaseName'),
            self.DBConfig.get ('Username'),
            self.DBConfig.get ('Password')
        )

    @property
    def Config (self) -> dict:
        with open ('Config.json', 'r') as Config:
            return json.load (Config)

    @property
    def DBConfig (self) -> dict:
        return self.Config.get ('Database')

    @property
    def Invite (self) -> str:
        return self.Config.get ('Invite')

    @property
    def Description (self) -> str:
        return self.Config.get ('Description')

    @property
    def Status (self) -> str:
        return self.Config.get ('Status')

    @property
    def Modules (self) -> dict:
        return self.Config.get ('Modules')

    def RegisterPlugin (self, Name: str, Description: str, Commands: list):
        self.Plugins.append ({
            'Name': Name,
            'Description': Description,
            'Commands': Commands
        })

    def LoadExtensions (self, Folder: str, Extensions: list, Suffix: str = ''):
        for Extension in Extensions:
            Path = f'{Folder}.{Extension}{Suffix}'

            try:
                self.load_extension (Path)
                Logs.Success (f'{Extension} was successfully loaded!')

            except Exception as Error:
                Logs.Error (f'{Extension} cannot be loaded!\n\tError: {Error}')

    def Run (self):
        Logs.Debug (f'Bot started at: {str (datetime.now ())}')

        Logs.Debug ('Removing command: help..')
        self.remove_command ('help')

        Logs.Debug ('Loading events file..')
        self.load_extension ('Events')

        Logs.Debug ('Loading commands..')
        self.LoadExtensions ('Modules.Commands', self.Modules.get ('Commands'), 'Command')

        Logs.Debug ('Loading plugins..')
        self.LoadExtensions ('Modules.Plugins', self.Modules.get ('Plugins'), 'Plugin')

        Logs.Debug ('Running bot..')
        self.run (self.Config.get ('Token'))
        Logs.Success ('Bot is running!')
