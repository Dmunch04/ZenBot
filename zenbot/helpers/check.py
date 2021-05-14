from discord.ext import commands

from zenbot.commands.command import ZenCommand
from zenbot.models import PermissionLevel, Member


def has_cache():
    async def predicate(cmd: commands.Command, ctx: commands.Context):
        if not ctx.bot.data_manager.servers.has(ctx.guild.id):
            await ctx.bot.data_manager.update_server_cache(ctx.bot, ctx.guild)

        if not ctx.bot.data_manager.servers.get(ctx.guild.id).members.has(
            ctx.author.id
        ):
            ctx.bot.data_manager.servers.get(ctx.guild.id).members.put(
                ctx.author.id, Member.new(ctx.author, ctx.guild), silent=True
            )

    return commands.before_invoke(predicate)


def has_permission():
    async def predicate(ctx: commands.Context):
        if not isinstance(ctx.cog, ZenCommand):
            raise ValueError("cog must be instance of ZenCommand")

        has_perm = await check_perms(ctx, ctx.command.qualified_name)

        if not has_perm:
            # TODO: should we even send a message like this? (if so it should be an embed)
            # (we shouldnt because it can also return false if the command isnt enabled)
            # await ctx.send("You don't have permission to use this command")
            pass

        return has_perm

    return commands.check(predicate)


async def check_perms(ctx: commands.Context, cmd_name: str):
    server = ctx.bot.data_manager.servers.get(ctx.guild.id)
    user = server.members.get(ctx.author.id)

    cmd_map = server.cmd_map

    if cmd_name not in cmd_map:
        return False

    cmd_lvl = cmd_map[cmd_name]
    cmd_perm = ctx.bot.cmd_map[cmd_name].perm_str
    user_lvl = user.perm_level
    user_perms = user.perms

    if (
        await ctx.bot.is_owner(ctx.author)
        or (
            user_lvl != PermissionLevel.OWNER
            and ctx.channel.permissions_for(ctx.author).administrator
        )
        or cmd_lvl == PermissionLevel.INVALID
        or cmd_perm in user_perms
        or user_lvl >= cmd_lvl
    ):
        return True

    return False
