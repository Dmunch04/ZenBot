import discord

from Core.Models import Server

class Member:
    def __init__ (self, Client: discord.Client, Member: discord.Member, Server: Server):
        self.Client = Client
        self.Instance = Member
        self.ID = Member.id
        self.Server = Server

        # The time left of members tempban
        self.BanTimeLeft = 0
        # The time left of members tempmute
        self.MuteTimeLeft = 0

        self.Path = self.Server.Path + f'Members/{str (self.Instance.id)}-{self.Instance.name}#{self.Instance.discriminator}/'
        MemberPath = self.Path + 'Member.json'
        #self.Config = self.Client.LoadJsonFile (MemberPath)
