import discord
from discord.ext import commands

class PluginCommand (commands.Cog):
    def __init__ (self, Client):
        self.Client = Client

    @commands.command (pass_context = True)
    @commands.is_owner ()
    def install (self, ctx, *, _Plugin: str):
        """ This command installs an official plugin to this server """

        print (_Plugin)

        self.Client.Database.GetServer (ctx.guild.id).Plugins.Add ({
            'Name': str (_Plugin)
        })

    @commands.command (pass_context = True)
    @commands.is_owner ()
    def uninstall (self, ctx, *, _Plugin: str):
        """ This command uninstalls an official plugin from this server """

        self.Client.Database.GetServer (ctx.guild.id).Plugins.Add ({
            'Name': str (_Plugin)
        })

def setup (_Client):
    _Client.add_cog (PluginCommand (_Client))
