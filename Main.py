import sys

# Discord Imports
import discord
from discord.ext import commands

# Script Imports
import Config
import Setup

Token = Config.Token
Client = discord.Client ()
client = commands.Bot (command_prefix = Config.Prefix)

client.remove_command ('help')

@client.event
async def on_ready ():
    await client.change_presence (game = discord.Game (name = '{0}help'.format (Config.Prefix)))

    print ("Bot's been booted up. Awaiting user interaction")

if __name__ == '__main__':
    Setup.Setup ()

    #client.load_extension (Config.Path_Events_Script)
    client.load_extension ('Events')

    FailedFiles = []

    for Command in Config.Commands:
        Command = '{0}.{1}Command'.format (Config.Commands_Folder, Command)

        print (Command)
        client.load_extension (Command)

        try:
            client.load_extension (Command)
        except Exception as Error:
            ErrorMsg = '{0} cannot be loaded. Error: {0}'.format (Command, Error)
            print (ErrorMsg)
            FailedFiles.append (ErrorMsg)

    with open ('NonLoadedCommands.txt', 'w') as File:
        File.write ('\n'.join (FailedFiles))

    client.run (Token)
