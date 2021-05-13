import discord
from discord.ext import commands


def get_prefix(bot: commands.Bot, message: discord.Message):
    prefix: str = "!"
    if message.guild is None or message is None:
        return prefix

    # TODO: Get server prefix
    prefix = "!"
    return prefix
