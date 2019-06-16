import discord

from Core.Utilities import Collection

class Plugin:
    def __init__ (self, Name: str, Version: str, Author: str, Description: str, BotVersion: str, Username: str, Repo: str, Branch: str):
        self.Name = Name
        self.Version = Version
        self.Author = Author
        self.Description = Description
        self.BotVersion = BotVersion
        self.Username = Username
        self.Repo = Repo
        self.Branch = Branch

        self.Command = f'git clone https://github.com/{self.Username}/{self.Repo} '
        self.Command += f'Data/Servers/!!!/Plugins/{self.Username}-{self.Repo}-{self.Branch} '
        self.Command += f'-b {self.Branch} -q'

class PluginDatabase:
    def __init__ (self, Client: discord.Client):
        self.Client = Client

        self.Plugins = Collection (Plugin)