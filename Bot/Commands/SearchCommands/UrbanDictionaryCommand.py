import urbandictionary as urban

import discord
from discord.ext import commands

from Helpers import EmbedHelper as Embed

class UrbanDictionaryCommand (commands.Cog):
    def __init__ (self, Client : discord.Client):
        self.Client = Client

    @commands.command (aliases = ['urban', 'urbandict'])
    async def urbandictionary (self, ctx: commands.Context, *, _Search: str):
        Channel = ctx.channel

        UrbanDefinitions = urban.define (_Search)

        if UrbanDefinitions:
            Definition = UrbanDefinitions[0]

            DefinitionText = Definition.definition[0 : 100]
            DefinitionText += '...' if len (Definition.definition) > 100 else ''
            Link = f'https://www.urbandictionary.com/define.php?term={_Search.lower ()}'
            DefinitionText += f'\n[Read More]({Link})' if len (Definition.definition) > 100 else ''

        await Embed.Embed (
            f'Urban Dictionary result of: {_Search}',
            '',
            discord.Color.blue (),
            Channel,
            self.Client,
            [
                ('Definition', DefinitionText),
                ('Example', Definition.example),
                ('Link', Link),
                ('Rating', f'👍 {str (Definition.upvotes)}     -     👎 {str (Definition.downvotes)}')
            ]
        )

    @commands.command (aliases = ['urbandef', 'udef'])
    async def urbandefinition (self, ctx: commands.Context, *, _Search: str):
        Channel = ctx.channel

        UrbanDefinitions = urban.define (_Search)

        if UrbanDefinitions:
            Definition = UrbanDefinitions[0].definition

        await Embed.Embed (
            f'Urban Dictionary definition of: {_Search}',
            Definition,
            discord.Color.blue (),
            Channel,
            self.Client
        )

def setup (_Client):
    _Client.add_cog (UrbanDictionaryCommand (_Client))
