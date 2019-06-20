import nltk
nltk.download ('wordnet')
from nltk.corpus import wordnet
from PyDictionary import PyDictionary

import discord
from discord.ext import commands

from Core import CommandEnabled
from Helpers import EmbedHelper as Embed

class DictionaryCommand (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @commands.command (aliases = ['dict', 'meaning'])
    @commands.check (CommandEnabled)
    async def dictionary (self, ctx: commands.Context, *, _Search: str):
        Channel = ctx.channel

        Dictionary = PyDictionary ()
        Definitions = Dictionary.meaning (_Search)
        DefinitionList = []

        if isinstance (Definitions, dict):
            for fos in Definitions:
                DefinitionList.append([fos, Definitions[fos][0]])

        await Embed.Embed (
            f'Definition of: {_Search}',
            DefinitionList[0],
            discord.Color.blue (),
            Channel,
            self.Client
        )

    @commands.command (aliases = ['syn'])
    @commands.check (CommandEnabled)
    async def synonym (self, ctx: commands.Context, *, _Search: str):
        Channel = ctx.channel

        Synonyms = []

        for Synonym in wordnet.synsets (_Search):
            for Lemma in Synonym.lemmas ():
                Synonyms.append (Lemma.name ())

        await Embed.Embed (
            f'Synonym of: {_Search}',
            str (Synonyms[0]),
            discord.Color.blue (),
            Channel,
            self.Client
        )

    @commands.command (aliases = ['ant'])
    @commands.check (CommandEnabled)
    async def antonym (self, ctx: commands.Context, *, _Search: str):
        Channel = ctx.channel

        Antonyms = []

        for Synonym in wordnet.synsets (_Search):
            for Lemma in Synonym.lemmas ():
                if Lemma.antonyms ():
                    Antonyms.append (Lemma.antonyms ()[0].name ())

        await Embed.Embed (
            f'Antonym of: {_Search}',
            str (Antonyms[0]),
            discord.Color.blue (),
            Channel,
            self.Client
        )

def setup (_Client):
    _Client.add_cog (DictionaryCommand (_Client))
