from typing import List, NoReturn

from discord.ext import commands

from zenbot.models import PermissionLevel
from zenbot.helpers import has_cache, check_perms
from .command import ZenCommand, ZenCommandParameter


class MuteCommand(commands.Cog, ZenCommand):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command("mute")
    @has_cache()
    async def help(
        self,
        ctx: commands.Context,
        *,
        user_id: str,
        duration: str = "10m",
        reason: str = "Unreasoned",
    ):
        if not await check_perms(ctx, self.name):
            # TODO: embed error
            await ctx.send("you dont have perms :P")
            return False

        author = ctx.author
        channel = ctx.channel
        server = ctx.guild

    @property
    def name(self) -> str:
        return "mute"

    @property
    def description(self) -> str:
        return "Mute a user from chatting in any channels for a specified duration"

    @property
    def category(self) -> str:
        return "Moderation"

    @property
    def parameters(self) -> List[ZenCommandParameter]:
        return [
            ZenCommandParameter(
                "user", "The ID of the user to be muted", required=True
            ),
            ZenCommandParameter("duration", "The duration of the mute", default="10m"),
            ZenCommandParameter(
                "reason", "The reason for the mute", default="Unreasoned"
            ),
        ]

    @property
    def perm_str(self) -> str:
        return "cmd.mute"

    @property
    def perm_level(self) -> PermissionLevel:
        return PermissionLevel.MODERATOR

    @property
    def example(self) -> str:
        return "{prefix}mute 842786340097097798 1d spam"


def setup(bot: commands.Bot) -> NoReturn:
    bot.add_cog(MuteCommand(bot))
