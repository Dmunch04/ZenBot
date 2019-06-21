import datetime

import discord
from discord.ext import commands

from Core import CommandEnabled
from Helpers import EmbedHelper as Embed

class SupportCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @commands.command ()
    @commands.check (CommandEnabled)
    async def support (self, ctx: commands.Context, *, _Description: str):
        Server = ctx.guild
        Sender = ctx.author

        ServerInstance = await self.Client.Database.GetServer (Server.id)

        ID = str (ServerInstance.Config.get ('SupportID', 1))
        Name = f'support-{ID}'
        Overwrites = {
            ServerInstance.Instance.default_role: discord.PermissionOverwrite (read_messages = False, send_messages = False),
            Sender: discord.PermissionOverwrite (read_messages = True, send_messages = True)
        }

        #Category = await ServerInstance.Instance.create_category ('Supports')

        Channel = await ServerInstance.Instance.create_text_channel (Name, overwrites = Overwrites)
        await Embed.Embed (
            'Support channel!',
            'A new support ticket has been opened!',
            discord.Color.green (),
            Channel,
            self.Client,
            [
                ('Description', _Description),
                ('Creator', Sender.mention),
                ('Date Created', datetime.datetime.now ())
            ]
        )

        await ServerInstance.Set (ctx, self.Client, 'config', 'supportid', str (int (ID) + 1), True)

    @commands.command ()
    @commands.check (CommandEnabled)
    async def close (self, ctx: commands.Context, _Archive: bool = False):
        Channel = ctx.channel

        if Channel.name.startswith ('support-'):
            if not _Archive:
                await Channel.delete (reason = 'Support ticket has been closed')

            else:
                # Kick the creator member
                pass

def setup (_Client):
    _Client.add_cog (SupportCommand (_Client))
