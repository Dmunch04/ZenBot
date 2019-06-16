from enum import IntEnum

import discord
from discord.ext import commands

class PermissionLevel (IntEnum):
    Owner = 5
    Admin = 4
    Moderator = 3
    Supporter = 2
    Default = 1
    Invalid = -1
