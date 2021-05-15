import os
from datetime import datetime
from typing import NoReturn, List, Dict

import discord
from discord.ext import commands

from .commands import ZenCommand
from .data import config
from .db import DataManager
from .logging import LogManager
from .utils.prefix import get_prefix


# TODO: what happens if a user joins the server while updating the members cache?
# TODO: disallow most of the commands in DMs (except for maybe a `info` command)
# TODO: currently the bot generates 2 new DB objects when a server is being added for the first time
#  (NOTE: i think this only happens when the first message is a command,
#         because new servers both gets handled async in the on_message and before a command is invoked)

# TODO: i accidentally messed up the imports lol


class ZenBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=get_prefix,
            description=config.bot_description,
            activity=discord.Game(name=config.status),
            case_insensitive=True,
            max_messages=10_000,
            intents=discord.Intents(
                bans=True,
                dm_messages=True,
                dm_reactions=True,
                emojis=True,
                guild_messages=True,
                guild_reactions=True,
                guilds=True,
                invites=True,
                members=True,
                messages=True,
                presences=True,
                reactions=True,
            ),
        )

        self.data_manager = DataManager()
        self.logger = LogManager()

        self._cmd_map = None

    @property
    def cmd_map(self) -> Dict[str, ZenCommand]:
        if not self._cmd_map:
            self._cmd_map = {}
            for cog_name in self.cogs:
                cog = self.get_cog(cog_name)
                if isinstance(cog, ZenCommand):
                    self._cmd_map[cog.name] = cog

        return self._cmd_map

    @property
    def simple_cmd_map(self) -> Dict[str, int]:
        simple_cmd_map = {}
        for name, cmd in self.cmd_map.items():
            simple_cmd_map[name] = int(cmd.perm_level)

        return simple_cmd_map

    def load_dir_exts(self, folder: str, ignore: List[str] = None) -> NoReturn:
        if ignore is None:
            ignore = []

        for ext in os.listdir(folder):
            if ext.startswith("__") or not ext.endswith(".py") or ext in ignore:
                continue

            ext = ".".join(ext.split(".")[:-1])

            try:
                self.load_extension(f"{folder.replace('/', '.')}{ext}")
                self.logger.success(f"{ext} was successfully loaded!")
            except Exception as e:
                self.logger.error(f"{ext} cannot be loaded!\n\tError: {e}")

    def startup(self) -> NoReturn:
        self.logger.debug(f"Bot started at: {str(datetime.now())}")

        self.logger.debug("Removing command: help..")
        self.remove_command("help")

        self.logger.debug("Loading events file..")
        self.load_extension("zenbot.events")

        self.logger.debug("Loading commands..")
        self.load_dir_exts("zenbot/commands/", ignore=["command.py"])

        self.logger.debug("Loading modules..")
        self.load_dir_exts("zenbot/modules/", ignore=[])

        self.logger.debug("Running bot..")
        self.run(config.get("token"))
        self.logger.server("Bot exited!")
