import discord

def Embed (_Title: str, _Content: str, _Color, _Channel: discord.TextChannel):
    Embed = discord.Embed (
        title = _Title,
        description = _Content,
        colour = _Color
    )

    _Channel.send (_Channel, embed = Embed)
