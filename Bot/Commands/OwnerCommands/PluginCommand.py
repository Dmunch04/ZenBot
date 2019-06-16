import discord
from discord.ext import commands

class PluginCommand (commands.Cog):
    def __init__ (self, Client, GlobalDatabase):
        self.Client = Client
        self.GlobalDatabase = GlobalDatabase

    @commands.command (pass_context = True)
    @commands.is_owner ()
    async def install (self, ctx, *, _Plugin: str):
        """ This command installs an official plugin to this server """

        _Plugin = str (_Plugin)

        Server = await self.Client.Database.GetServer (ctx.guild.id).Plugins

        if _Plugin in self.GlobalDatabase.Plugins:
            if not _Plugin in Server.GetAll ():
                CurPlugin = self.GlobalDatabase.Plugins[_Plugin]

                PluginToAdd = Plugin (
                    CurPlugin['Name'],
                    CurPlugin['Version'],
                    CurPlugin['Author'],
                    CurPlugin['Description'],
                    CurPlugin['BotVersion'],
                    CurPlugin['Username'],
                    CurPlugin['Repo'],
                    CurPlugin['Branch']
                )

                await Server.Add (PluginToAdd)

                # Run the plugins command

    @commands.command (pass_context = True)
    @commands.is_owner ()
    async def uninstall (self, ctx, *, _Plugin: str):
        """ This command uninstalls an official plugin from this server """

        Server = await self.Client.Database.GetServer (ctx.guild.id).Plugins

        if _Plugin in self.GlobalDatabase.Plugins:
            if _Plugin in Server.GetAll ():
                await Server.Remove (_Plugin)

                # Remove the folder

def setup (_Client):
    _Client.add_cog (PluginCommand (_Client, _Client.Database))
