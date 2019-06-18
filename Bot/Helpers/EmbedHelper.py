import discord

async def Embed (_Title: str, _Content: str, _Color, _Channel: discord.TextChannel, _Client: discord.Client = None, _Fields: list = []):
    Embed = discord.Embed (
        title = _Title,
        description = _Content,
        colour = _Color
    )

    if _Client:
        Embed.set_author (
            name = _Client.user.name,
            url = _Client.Website,
            icon_url = _Client.user.avatar_url
        )

    if _Fields:
        for Field in _Fields:
            Embed.add_field (
                name = Field[0],
                value = Field[1]
            )

    _Channel.send (embed = Embed)

async def DMEmbed (_Title: str, _Content: str, _Color, _Member: discord.Member, _Client: discord.Client = None, _Fields: list = []):
    Embed = discord.Embed (
        title = _Title,
        description = _Content,
        colour = _Color
    )

    if _Client:
        Embed.set_author (
            name = _Client.user.name,
            url = _Client.Website,
            icon_url = _Client.user.avatar_url
        )

    if _Fields:
        for Field in _Fields:
            Embed.add_field (
                name = Field[0],
                value = Field[1]
            )

    await _Member.create_dm ()
    await _Member.dm_channel.send (embed = Embed)
