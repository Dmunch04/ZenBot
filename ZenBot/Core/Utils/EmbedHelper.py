import discord
from discord.ext import commands

async def CreateEmbed (Title: str, Content: str, Color: discord.Color, Client: commands.Bot = None, Fields: list = None) -> discord.Embed:
    Embed = discord.Embed (
        title = Title,
        description = Content,
        color = Color
    )

    if Client:
        """
        Embed.set_author (
            name = Client.user.name,
            url = Client.Website,
            icon_url = Client.user.avatar_url
        )
        """
        Embed.set_footer (
            text = Client.user.name,
            icon_url = Client.user.avatar_url
        )

    if Fields:
        for Field in Fields:
            Embed.add_field (
                name = Field['Name'],
                value = Field['Value'],
                inline = False
            )

    return Embed

async def MakeEmbed (Title: str, Content: str, Color: discord.Color, Channel: discord.TextChannel, Client: commands.Bot = None, Fields: list = None):
    Embed = await CreateEmbed (Title, Content, Color, Client, Fields)

    await Channel.send (embed = Embed)

async def MakeDMEmbed (Title: str, Content: str, Color: discord.Color, User: discord.User, Client: commands.Bot = None, Fields: list = None):
    Embed = await CreateEmbed (Title, Content, Color, Client, Fields)

    await User.create_dm ()
    await User.dm_channel.send (embed = Embed)