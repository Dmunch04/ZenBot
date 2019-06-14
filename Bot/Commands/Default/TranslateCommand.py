import discord
from discord.ext import commands

from Modules import CommandCheck as cmd
from Modules import Translator as trans
from Helpers import EmbedHelper as embed

class CMD_Translate:
    def __init__ (self, Client):
        self.Client = Client

    @commands.command()
    async def translate (self, ctx, _From, _To, *_Text):
        Server = ctx.guild
        Channel = ctx.channel

        if cmd.CheckCommand ('Translate', Server.id) == False:
            return

        if not _From.lower () in trans.Languages:
            embed.CustomErrorEmbed (self.Client, 'Unkown Language', 'Unkown Language', 'We don\'t support this language: ' + _From, Channel)

        if not _To.lower () in trans.Languages:
            embed.CustomErrorEmbed (self.Client, 'Unkown Language', 'Unkown Language', 'We don\'t support this language: ' + _To, Channel)

        # Translate
        Text = ''.join (_Text)
        Translation = trans.Translate (_From, _To, Text)

        if Translation:
            embed.OtherEmbed (self.Client, 'Translation', f'Here\'s the translation of {Text} from {_From} to {_To}', Translation, discord.Color.green (), Channel)

        else:
            embed.ErrorEmbed (self.Client, 'Translate', Channel)

def setup (_Client):
    _Client.add_cog (CMD_Translate (_Client))
