import discord
from discord.ext import commands

from Core import CommandEnabled
from Core.Utils import Helper, Color
from Core.Utils.EmbedHelper import MakeEmbed

class HelpCommand (commands.Cog):
    def __init__ (self, Client: commands.Bot):
        self.Client = Client

    @commands.command ()
    @commands.check (CommandEnabled)
    async def help (self, ctx: commands.Context):
        Commands = []
        for Command in self.Client.Modules.get ('Commands'):
            Commands.append (Helper.GetPrefix (self.Client, ctx.message) + Command)

        await MakeEmbed (
            'Help',
            'Help embed here :)',
            Color.DarkGrey,
            ctx.channel,
            self.Client,
            [
                {
                    'Name': 'Commands',
                    'Value': '\n'.join (Commands)
                }
            ]
        )

def setup (Client: commands.Bot):
    Client.add_cog (HelpCommand (Client))