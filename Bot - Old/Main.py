import sys
from DavesLogger import Logs

# Discord Imports
import discord
from discord.ext import commands

# Script Imports
import Config
import Setup

Token = Config.Token
Client = commands.Bot (command_prefix = Config.Prefix)

@Client.event
async def on_ready ():
    await Client.change_presence (game = discord.Game (name = '{0}help'.format (Config.Prefix)))

    Logs.Server ('The bot has been booted!')

if __name__ == '__main__':
    Setup.Setup ()

    Client.remove_command ('help')
    Client.load_extension ('Events')

    FailedFiles = []

    for Command in Config.Commands:
        Command = '{0}.{1}Command'.format (Config.Commands_Folder, Command)

        try:
            Client.load_extension (Command)

        except Exception as Error:
            ErrorMsg = '{0} cannot be loaded. Error: {0}'.format (Command, Error)
            Logs.Error (ErrorMsg)

            FailedFiles.append (Command)

    print (FailedFiles)

    Client.run (Token)
