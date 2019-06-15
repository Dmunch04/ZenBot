import discord

def CheckRole (_User : discord.Member, _Role):
    if _Role in [Role.name.lower () for Role in _User.roles]:
        return True
    else:
        return False
