import discord
from discord.ext import commands
from typing import List, NoReturn
from .command import ZenCommand, ZenCommandParameter
from zenbot.models import PermissionLevel


class HelpCommand(commands.Cog, ZenCommand):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command("help")
    async def help(self, ctx: commands.Context, *, name: str = None):
        author = ctx.author
        channel = ctx.channel
        server = ctx.guild

        # cmd_map = {self.bot.get_cog(cog).name: self.bot.get_cog(cog) for cog in self.bot.cogs if isinstance(self.bot.get_cog(cog), ZenCommand)}
        """
        cmd_map = {}
        for cog_name in self.bot.cogs:
            cog = self.bot.get_cog(cog_name)
            if isinstance(cog, ZenCommand):
                cmd_map[cog.name] = cog
        """

        if name:
            await ctx.send(self.bot.cmd_map[name].signature)
        else:
            for cmd in self.bot.cmd_map.values():
                await ctx.send(cmd.signature)

    @property
    def name(self) -> str:
        return "help"

    @property
    def description(self) -> str:
        return "A general help command"

    @property
    def category(self) -> str:
        return "Basic"

    @property
    def parameters(self) -> List[ZenCommandParameter]:
        return [
            ZenCommandParameter(
                "cmd", "A command to be shown further helpful information of"
            )
        ]

    @property
    def perm_str(self) -> str:
        return "cmd.help"

    @property
    def perm_level(self) -> PermissionLevel:
        return PermissionLevel.GUEST

    @property
    def example(self) -> str:
        # TODO: should we get the prefix here instead?
        return "{prefix}help"


def setup(bot: commands.Bot) -> NoReturn:
    bot.add_cog(HelpCommand(bot))
