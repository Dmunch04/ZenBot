# Discord Imports
import discord

# Lib Imports
import json

# Script Imports
import Config

# Embeds

# -- Search Result Embeds --

# Embed for positive search results
async def ResultLinkEmbed (_Client, _Type, _Title, _Content, _Link, _Channel):
    Embed = discord.Embed (title = _Title, url = _Link, description = _Content, color = discord.Color.green ())
    Embed.set_author (name = _Type + ' Result:')

    await _Client.send_message (_Channel, embed = Embed)

# Embed for when an urban dictionary result is found. This needs a custom template
async def UrbanEmbed (_Client, _Word, _Definition, _Example, _Upvotes, _Downvotes, _Channel):
    Embed = discord.Embed (color = discord.Color.green ())
    Embed.set_author (name = 'UrbanDictionary Result:')
    Embed.add_field (name = 'Searched word:', value = _Word, inline = False)
    Embed.add_field (name = 'Definition:', value = _Definition, inline = False)
    Embed.add_field (name = 'Usage Example:', value = _Example, inline = False)
    Embed.add_field (name = 'Rating:', value = f'👍{_Upvotes}   👎{_Downvotes}', inline = False)

    await _Client.send_message (_Channel, embed = Embed)

async def YoutubeChannel (_Client, _Name, _Subs, _Videos, _Link, _Channel):
    Embed = discord.Embed (color = discord.Color.green ())
    Embed.set_author (name = 'Youtube Channel:')
    Embed.add_field (name = 'Channel Name:', value = _Name, inline = False)
    Embed.add_field (name = 'Subscribers:', value = _Subs, inline = False)
    Embed.add_field (name = 'Videos:', value = _Videos, inline = False)
    Embed.add_field (name = 'Link:', value = _Link, inline = False)

    await _Client.send_message (_Channel, embed = Embed)


# -- Other Embeds --

# Embed for announcement messages
async def AnnouncementEmbed (_Client, _Title, _Message, _Channel):
    Embed = discord.Embed(title = _Title, description = _Message, color = 0x2a2a2a)

    await _Client.send_message (_Channel, embed = Embed)

# Embed for file messages. Ex. help and rules messages
async def ListEmbed (_Client, _Path, _Channel):
    Messages = json.load (_Path)

    Embed = discord.Embed (color = discord.Color.purple ())
    Embed.set_author (name = Messages['Title'])

    # Find a way to check if the message is a help message. If so, then
    # add the prefix from Config in front of the name!

    for Item in Messages:
        if Item == 'Title': continue

        Embed.add_field (name = Item, value = Messages[Item], inline = False)

    await _Client.send_message (_Channel, embed = Embed)

# Embed for the user info message. This needs a custom template
async def UserEmbed (_Client, _Name, _Tag, _Roles, _Karma, _Activity, _Warns, _Channel):
    Embed = discord.Embed (color = _Color)
    Embed.set_author (name = f"{_Name}#{_Tag}'s Info:")
    Embed.add_field (name = 'Name', value = _Name, inline = False)
    Embed.add_field (name = 'Tag', value = _Tag, inline = False)
    Embed.add_field (name = 'Roles', value = _Roles, inline = False)
    Embed.add_field (name = 'Karma', value = _Karma, inline = False)
    Embed.add_field (name = 'Activity', value = _Activity, inline = False)
    Embed.add_field (name = 'Warns', value = _Warns, inline = False)

    await _Client.send_message (_Channel, embed = Embed)

# Embed for the server info message. This needs a custom template
async def ServerEmbed (_Client, _Server, _Channel):
    Embed = discord.Embed (color = 0x2a2a2a)
    Embed.set_author (name = f'About {_Server.name}:')
    Embed.add_field (name = 'Name', value = _Server.name, inline = False)
    Embed.add_field (name = 'Users', value = _Server.member_count, inline = False)
    Embed.add_field (name = 'Owner', value = f'{_server.owner.name}#{_server.owner.discriminator}', inline = False)
    Embed.add_field (name = 'Region', value = _Server.region, inline = False)
    Embed.add_field (name = 'Invite', value = discord.invites_from (_Server)[0], inline = False) # Get the invite

    await _Client.send_message (_Channel, embed = Embed)

# Embed for other embed messages. This can be anything
async def OtherEmbed (_Client, _Title, _MessageTitle, _Message, _Color, _Channel):
    Embed = discord.Embed (title = _MessageTitle, description = _Message, color = _Color)
    Embed.set_author (name = _Title)

    await _Client.send_message (_Channel, embed = Embed)


# -- Error Embeds --

# Embed that finds all the error stuff from Config
async def ErrorEmbed (_Client, _Type, _Channel):
    Title = Config.Errors[_Type]['Title']
    Type = Config.Errors[_Type]['Type']
    Error = Config.Errors[_Type]['Error']
    Code = Config.Errors[_Type]['Code']

    Embed = discord.Embed (title = Title, description = Error, color = discord.Color.red ())
    Embed.set_author (name = Type)

    await _Client.send_message (_Channel, embed = Embed)

# Embed for the error: Specify Error (When you don't specify what you wanna search for)
async def SpecifyErrorEmbed (_Client, _Channel):
    Embed = discord.Embed (title = 'Specify Search', description = 'Please specify what you wanna search for!', color = discord.Color.red ())
    Embed.set_author (name = 'Command Error')

    await _Client.send_message (_Channel, embed = Embed)

# Embed for the error: Permission Error (When you don't have the required role for the command)
async def PermissionErrorEmbed (_Client, _Channel):
    Embed = discord.Embed (title = 'No Permission', description = "Looks like you don't have the permission for that command!", color = discord.Color.red ())
    Embed.set_author (name = 'Permission Error')

    await _Client.send_message (_Channel, embed = Embed)

# Embed for the error: Result Error (When the search commands result is empty)
async def ResultErrorEmbed (_Client, _Channel):
    Embed = discord.Embed (title = 'No Result', description = "Looks like we couldn't find what you searched for.", color = discord.Color.red ())
    Embed.set_author (name = 'Result Error')

    await _Client.send_message (_Channel, embed = Embed)

# Embed for the error : Unknown Error (When no one knows the error)
async def UnknownErrorEmbed (_Client, _Channel):
    Embed = discord.Embed (title = 'Something went wrong..', description = 'Whoops! Looks like something went wrong.', color = discord.Color.red ())
    Embed.set_author (name = 'Command Error')

    await _Client.send_message (_Channel, embed = Embed)

# Embed for a custom error. This can be anything
async def CustomErrorEmbed (_Client, _Title, _ErrorTitle, _Error, _Channel):
    Embed = discord.Embed (title = _ErrorTitle, description = _Error, color = discord.Color.red ())
    Embed.set_author (name = _Title)

    await _Client.send_message (_Channel, embed = Embed)
