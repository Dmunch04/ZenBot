import random
import eve

# Discord Imports
from discord.ext import commands

# Module Imports
import Config
from Modules import FileHandler as filing
from Modules import RoleCheck as role
from Helpers import EmbedHelper as embed

class Events:
    def __init__ (self, Client):
        self.Client = Client

    async def on_message (self, _Message):
        Server = _Message.guild
        Channel = _Message.channel
        Sender = _Message.author

        if Sender.bot: return

        XP = random.randint (Config.Message_XP_Amount[0], Config.Message_XP_Amount[1])

        Path = Config.Path_Data_Servers + '/' + Server.id
        UserPath = Path + '/Users/' + Sender.name + '#' + Sender.discriminator + '/' + 'UserFile.eve'

        Data = eve.load (UserPath)

        Data['Activity'] = int (Data['Activity']) + int (XP)

        eve.save (Data, UserPath)

        Data = eve.load (Path + '/settings.eve')

        if Data['ProfanityFiler'] == True:
            if any (Word in _Message.content.lower () for Word in Config.Bad_Words):
                await _Message.delete()

        await self.Client.process_commands (_Message)

    async def on_member_join (self, _Member):
        if _Member.bot: return

        filing.AddMember (_Member)

    async def on_member_leave (self, _Member):
        filing.RemoveMember (_Member)

    async def on_member_update (self, _Before, _After):
        filing.UpdateMember (_Before, _After)

    async def on_guild_join (self, _Server):
        filing.AddServer (_Server)

    async def on_guild_remove (self, _Server):
        filing.RemoveServer (_Server)

    async def on_guild_update (self, _Before, _After):
        filing.UpdateServer (_Before, _After)

def setup (_Client):
    _Client.add_cog (Events (_Client))
