import discord
from discord.ext import commands

class TwitterPlugin (commands.Cog):
    def __init__ (self, Client: commands.Bot):
        self.Client = Client
        self.Client.RegisterPlugin ('Twitter', 'Uploads a Twitter tweet from a Twitter account when a new is tweeted!', [])

def setup (Client: commands.Bot):
    Client.add_cog (TwitterPlugin (Client))