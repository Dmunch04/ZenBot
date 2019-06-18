import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
from PyDictionary import PyDictionary

import discord
from discord.ext import commands

class DictionaryCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client
    
    @commands.command (aliases = ['dict', 'meaning'])
    async def dictionary (self, ctx : commands.Context, *, _Query : str):
        Dictionary = PyDictionary()

        Definitions = Dictionary.meaning(_Query)


        Embed = discord.Embed (
            title = f'Definition of: **{_Query}**',
            description = f''
        )
        Embed.set_author (
            name = self.Client.user.name,
            url = self.Client.Website,
            icon_url = self.Client.user.avatar_url
        )

        for key in Definitions:
            for definition in Definitions[key]:
                Embed.add_field (
                name = f'**{key}**',
                value = definition,
                inline = False
            )
            
        await ctx.send(embed = Embed)

    @commands.command (aliases = ['syn'])
    async def synonym (self, ctx : commands.Context, *, _Query : str): 
        Synonyms = ''

        for syn in wordnet.synsets(_Query):
            for l in syn.lemmas():
                Synonyms += f'{l.name()}\n'

        Embed = discord.Embed (
            title = f'Synonyms of: **{_Query}**',
            description = f'{Synonyms}'
        )
        Embed.set_author (
            name = self.Client.user.name,
            url = self.Client.Website,
            icon_url = self.Client.user.avatar_url
        )
            
        await ctx.send(embed = Embed)

    @commands.command (aliases = ['ant'])
    async def antonym (self, ctx : commands.Context, *, _Query : str):
        Antonyms = ''

        for syn in wordnet.synsets(_Query):
            for l in syn.lemmas():
                if l.antonyms():
                    Antonyms += f'{l.antonyms()[0].name()}\n'

        Embed = discord.Embed (
            title = f'Antonyms of: **{_Query}**',
            description = f'{Antonyms}'
        )
        Embed.set_author (
            name = self.Client.user.name,
            url = self.Client.Website,
            icon_url = self.Client.user.avatar_url
        )
            
        await ctx.send(embed = Embed)



def setup (_Client):
    _Client.add_cog( DictionaryCommand(_Client))
