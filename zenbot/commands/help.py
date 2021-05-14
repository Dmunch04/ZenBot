from typing import List, NoReturn

import discord
from discord.ext import commands

from zenbot.models import PermissionLevel
from zenbot.helpers import has_cache, check_perms
from .command import ZenCommand, ZenCommandParameter


class HelpCommand(commands.Cog, ZenCommand):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command("help")
    # @has_permission()
    @has_cache()
    async def help(self, ctx: commands.Context, *, name: str = None):
        if not await check_perms(ctx, self.name):
            # TODO: embed error
            await ctx.send("you dont have perms :P")
            return False

        cmd_map = self.bot.data_manager.servers.get(ctx.guild.id).cmd_map

        if name:
            if name in cmd_map:
                cmd = self.bot.cmd_map[name]

                if not await check_perms(ctx, name):
                    return

                param_str = ""
                for param in cmd.params:
                    param_str += "*" if param.required else ""
                    param_str += param.name + " - " + param.description
                    param_str += "\n"

                embed = discord.Embed(title=f"Help - `{cmd.name}` command")

                embed.add_field(name="Category", value=cmd.category)
                embed.add_field(name="Description", value=cmd.description)
                # TODO: why doesnt the embed wanna send when this field is added lol
                # embed.add_field(name="Parameters", value=param_str)
                # TODO: get prefix
                embed.add_field(name="Example", value=f"`{cmd.example}`")
                embed.add_field(name="Signature", value=f"`{cmd.signature}`")

                if ctx.channel.permissions_for(ctx.author).administrator:
                    embed.add_field(name="Permission String", value=f"`{cmd.perm_str}`")
                    embed.add_field(
                        name="Permission Level", value=f"`{cmd.perm_level.name}`"
                    )

                await ctx.author.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Help - List of available commands",
                description="Here's a list of all the commands of ZenBot that are available to you.",
            )

            categories = {}
            for name in cmd_map:
                if not await check_perms(ctx, name):
                    continue

                cmd = self.bot.cmd_map[name]
                if cmd.category not in categories:
                    categories[cmd.category] = []

                categories[cmd.category].append(cmd)

            for category in categories:
                cmds = categories[category]
                cmds_str = ""
                for cmd in cmds:
                    cmds_str += f"**{cmd.name}** - {cmd.description}\n"

                embed.add_field(name=category, value=cmds_str, inline=False)

            await ctx.author.send(embed=embed)

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
        return "{prefix}help"


def setup(bot: commands.Bot) -> NoReturn:
    bot.add_cog(HelpCommand(bot))
