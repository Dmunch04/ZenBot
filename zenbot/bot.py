import discord
from discord.ext import commands

from .context import ZenContext
from .logging import LogManager
from .utils.prefix import get_prefix
from .database import DataManager

import json
from datetime import datetime
from typing import (
    List,
    Dict,
    NoReturn,
    Any
)


class ZenBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=get_prefix,
            description=self.bot_description,
            activity=discord.Game(name=self.status),
            case_insensitive=True,
            max_messages=10_000
        )

        self.data_manager = DataManager(self.db_config)
        self.logger = LogManager()

    async def get_context(self, message, *, cls=ZenContext):
        return await super().get_context(message, cls=cls)

    def load_extensions(self, folder: str, extensions: List[str]) -> NoReturn:
        for extension in extensions:
            try:
                self.load_extension(f'zenbot.{folder}.{extension}')
                self.logger.success(f'{extension} was successfully loaded!')
            except Exception as e:
                self.logger.error(f'{extension} cannot be loaded!\n\tError: {e}')

    def startup(self):
        self.logger.debug(f'Bot started at: {str(datetime.now())}')

        self.logger.debug('Removing command: help..')
        self.remove_command('help')

        self.logger.debug('Loading events file..')
        self.load_extension('zenbot.events')

        self.logger.debug('Loading commands..')
        self.load_extensions('Modules.Commands', self.commands)

        self.logger.debug('Loading plugins..')
        self.load_extensions('Modules.Plugins', self.plugins)

        self.logger.debug('Running bot..')
        self.run(self.config.get('token'))
        self.logger.server('Bot exited!')

    @property
    def config(self) -> Dict[str, Any]:
        with open('./config.json', 'r') as config:
            return json.load(config)

    @property
    def bot_description(self) -> str:
        return self.config.get('description', '')

    @property
    def status(self) -> str:
        return self.config.get('status', '')

    @property
    def invite(self) -> str:
        return self.config.get('invite', '')

    @property
    def db_config(self) -> Dict[str, str]:
        return self.config.get('database', {})

    @property
    def modules(self) -> Dict[str, List[str]]:
        return self.config.get('modules', {})

    @property
    def commands(self) -> List[str]:
        return self.modules.get('commands', [])

    @property
    def plugins(self) -> List[str]:
        return self.modules.get('plugins', [])
