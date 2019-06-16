import logging

import discord
from discord.ext import commands

from Core.Models import PermissionLevel
from Core.Utilities import Error

Log = logging.getLogger ('ZenBot')

def HasPermission (_PermissionLevel: PermissionLevel = PermissionLevel.Default) -> bool:
    async def Predicate (ctx: commands.Context):
        HasPermssions = await CheckPermission (
            ctx,
            ctx.command.qualified_name,
            _PermissionLevel
        )

        if not HasPermssions and ctx.command.qualified_name != 'help':
            Log.error (
                Error (
                    f'You don\'t have permission to perform this command: '
                    f'`{ctx.command.qualified_name}` ({_PermissionLevel.name})!'
                )
            )

        return HasPermssions

    Predicate._PermissionLevel = _PermissionLevel

    return commands.check (Predicate)

async def CheckPermission (ctx: commands.Context, _CommandName: str, _PermissionLevel: PermissionLevel) -> bool:
    if await ctx.bot.is_owner (ctx.author):
        return True

    elif _PermissionLevel != PermissionLevel.Owner and ctx.channel.permissions_for (ctx.author).administrator:
        return True

    CommandPermissions = ctx.bot.config.command_permissions
    SenderRoles = ctx.author.roles

    if _CommandName in CommandPermissions:
        if -1 in CommandPermissions[_CommandName]:
            return True

        HasPermssionRole = any (
            Role.id in CommandPermissions[_CommandName] for Role in SenderRoles
        )

        HasPermssionID = ctx.author.id in CommandPermissions[_CommandName]

        return HasPermssionRole or HasPermssionID

    LevelPermissions = ctx.bot.config.level_permissions

    for Level in PermissionLevel:
        if Level >= _PermissionLevel and Level.name in LevelPermissions:
            if -1 in LevelPermissions[Level.name]:
                return True

            HasPermssionRole = any (
                Role.id in LevelPermissions[Level.name] for Role in SenderRoles
            )

            HasPermssionID = ctx.author.id in LevelPermissions[Level.name]

            if HasPermssionRole or HasPermssionID:
                return True

    return False
