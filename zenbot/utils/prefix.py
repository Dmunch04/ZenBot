import discord
from discord.ext import commands


async def get_prefix(bot: commands.Bot, message: discord.Message):
    prefix: str = "!"
    if message.guild is None or message is None:
        return prefix

    # TODO: wont this here actually just load all servers into cache anyway? so perhaps either retrieve it from the db
    #  or should we just have it load all the servers into cache this way and not care about the other system we setup?
    # TODO: this might actually be the cause to the issue with 2 objects of the same server in the db
    #  now that i think about it. so perhaps the on_message system should be removed and we just have this
    #  (together with the system before a command is invoked, just to make 100% sure)
    if not bot.data_manager.servers.has(message.guild.id):
        await bot.data_manager.update_server_cache(bot, message.guild)

    prefix = bot.data_manager.servers.get(message.guild.id).settings.prefix

    return prefix
