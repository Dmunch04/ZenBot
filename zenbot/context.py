import discord
from discord.ext import commands


class ZenContext(commands.Context):
    async def tick(self, cond: bool):
        emoji: str = '\N{WHITE HEAVY CHECK MARK}' if cond else '\N{CROSS MARK}'
        try:
            await self.message.add_reaction(emoji)
        except discord.HTTPException:
            pass
