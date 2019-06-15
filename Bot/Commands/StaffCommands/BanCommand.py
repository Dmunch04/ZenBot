import discord
from discord.ext import commands

class BanCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @commands.command ()
    async def ban (self, ctx, _Members = commands.Greedy[discord.Member], _DeleteDays: int = 0, *, _Reason: str = 'The ban hammer has spoken!'):
        """ Bans 1 or more members """

        # Send them a DM before?

        for Member in _Members:
            await Member.ban (delete_message_days = _DeleteDays, reason = _Reason)

def setup (_Client):
    _Client.add_cog (HelpCommand (_Client))
