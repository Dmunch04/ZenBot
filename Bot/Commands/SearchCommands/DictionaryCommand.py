import nltk
nltk.download ('wordnet')
from nltk.corpus import wordnet
from PyDictionary import PyDictionary

import discord
from discord.ext import commands

from Helpers import EmbedHelper as Embed

class DictionaryCommand (commands.Cog):
    def __init__ (self, Client: discord.Client):
        self.Client = Client

    @commands.command (aliases = ['dict', 'meaning'])
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
            '',
            discord.Color.blue (),
            Channel,
            self.Client,
            _Fields = DefinitionList
        )

    @commands.command (aliases = ['syn'])
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
