import googletrans

import discord
from discord.ext import commands

from Helpers import EmbedHelper as Embed

class TranslateCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (aliases = ['trans'])
    async def translate (self, ctx: commands.Context, _From: str = 'en', _To: str = 'en', *, _Text: str):
        Channel = ctx.channel

        Translator = googletrans.Translator ()
        Translation = Translator.translate (_Text, src = _From, dest = _To)

        await Embed.Embed (
            f'Translation of: {_Text}',
            Translation.text,
            discord.Color.blue (),
            Channel,
            self.Client
        )

def setup (_Client):
    _Client.add_cog (TranslateCommand (_Client))
