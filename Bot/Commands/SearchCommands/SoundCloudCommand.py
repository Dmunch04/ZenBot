import json
import urllib
import soundcloud

import discord
from discord.ext import commands

from Helpers import EmbedHelper as Embed

class SoundCloudCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @commands.command ()
    async def soundcloud (self, ctx: commands.Context, *, _Search: str):
        Channel = ctx.channel

        Client = soundcloud.Client (client_id = '175c043157ffae2c6d5fed16c3d95a4c')
        Song = Client.get ('/tracks', q = _Search)

        if Song.url:
            with urllib.request.urlopen (Song.url) as Data:
                Text = Data.read ()
                if Text:
                    Data = json.loads (Text.decode ('utf-8'))

        Item = Data[0]
        User = Item.get ('user', None)

        if User:
            Author = User.get ('username', 'NoName')

        Link = Item.get ('permalink_url', f'https://soundcloud.com/search?q={_Search.replace (" ", "%20")}')

        if len (Song) > 1:
            Song = Song[0]

        await Embed.Embed (
            f'SoundCloud result of: {_Search}',
            f'',
            discord.Color.blue (),
            Channel,
            self.Client,
            [
                ('Title', Song.title),
                ('Author', Author),
                ('Link', Link)
            ]
        )

def setup (_Client):
    _Client.add_cog (SoundCloudCommand (_Client))
