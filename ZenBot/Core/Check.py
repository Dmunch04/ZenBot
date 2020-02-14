from DavesLogger import Logs
from discord.ext import commands

from Core.Models import PermissionLevel

def HasPermission (PermLevel: PermissionLevel = PermissionLevel.Default) -> bool:
    async def Predicate (ctx: commands.Context):
        HasPermissions = await CheckPermission (
            ctx,
            ctx.command.qualified_name,
            PermLevel
        )

        if not HasPermissions and ctx.command.qualified_name != 'help':
            Logs.Error (f'You don\'t have permission to perform this command: \n{ctx.command.qualified_name}` ({PermLevel.name})!')

        return HasPermissions

    Predicate._PermissionLevel = PermLevel

    return commands.check (Predicate)

async def CheckPermission (ctx: commands.Context, CommandName: str, PermLevel: PermissionLevel) -> bool:
    if await ctx.bot.is_owner (ctx.author):
        return True

    elif PermLevel != PermissionLevel.Owner and ctx.channel.permissions_for (ctx.author).administrator:
        return True

    CommandPermissions = ctx.bot.config.command_permissions
    SenderRoles = ctx.author.roles

    if CommandName in CommandPermissions:
        if -1 in CommandPermissions[CommandName]:
            return True

        HasPermissionRole = any (
            Role.id in CommandPermissions[CommandName] for Role in SenderRoles
        )

        HasPermissionID = ctx.author.id in CommandPermissions[CommandName]

        return HasPermissionRole or HasPermissionID

    LevelPermissions = ctx.bot.config.level_permissions

    for Level in PermissionLevel:
        if Level >= PermLevel and Level.name in LevelPermissions:
            if -1 in LevelPermissions[Level.name]:
                return True

            HasPermissionRole = any (
                Role.id in LevelPermissions[Level.name] for Role in SenderRoles
            )

            HasPermissionID = ctx.author.id in LevelPermissions[Level.name]

            if HasPermissionRole or HasPermissionID:
                return True

    return False

async def CommandEnabled (ctx: commands.Context) -> bool:
    # TODO: Make this :)
    return True