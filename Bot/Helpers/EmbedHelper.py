import discord

def Embed (_Client: discord.Bot, _Title: str, _Content: str, _Color, _Channel: discord.Channel):
    Embed = discord.Embed (
        title = _Title,
        description = _Content,
        colour = _Color
    )

    _Client.send_message (_Channel, embed = Embed)
