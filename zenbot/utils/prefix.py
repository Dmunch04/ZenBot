import discord
from discord.ext import commands


async def get_prefix(bot: commands.Bot, message: discord.Message):
    prefix: str = "!"
    if message.guild is None or message is None:
        return prefix

    # TODO: wont this here actually just load all servers into cache anyway? so perhaps either retrieve it from the db
    #  or should we just have it load all the servers into cache this way and not care about the other system we setup?
    if not bot.data_manager.servers.has(message.guild.id):
        await bot.data_manager.update_server_cache(bot, message.guild)

    prefix = bot.data_manager.servers.get(message.guild.id).settings.prefix

    return prefix
