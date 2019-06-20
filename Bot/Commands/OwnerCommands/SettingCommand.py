import discord
from discord.ext import commands

from Helpers import EmbedHelper as Embed

class SettingCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @commands.command ()
    @commands.is_owner ()
    async def set (self, ctx: commands.Context, _Type: str, _Sub: str, *, _Value: str):
        Server = ctx.guild

        ServerInstance = await self.Client.Database.GetServer (Server.id)
        await ServerInstance.Set (_Type, _Sub, _Value)

    @commands.command ()
    @commands.is_owner ()
    async def get (self, ctx: commands.Context, _Type: str, _Sub: str = ''):
        Server = ctx.guild
        Sender = ctx.author

        ServerInstance = await self.Client.Database.GetServer (Server.id)
        Object = await ServerInstance.Get (_Type, _Sub)

        await Embed.DMEmbed (
            f'Got settings object: {_Type}{f" - {_Sub}" if _Sub else ""}',
            str (Object),
            discord.Color.purple (),
            Sender,
            self.Client
        )

def setup (_Client):
    _Client.add_cog (SettingCommand (_Client))
