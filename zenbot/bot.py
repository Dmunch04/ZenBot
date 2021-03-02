import os

import discord
from discord.ext import commands

from .context import ZenContext
from .logging import LogManager
from .utils.prefix import get_prefix
from .db import DataManager
from .data import config

from datetime import datetime
from typing import (
    NoReturn,
)


class ZenBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=get_prefix,
            description=config.bot_description,
            activity=discord.Game(name=config.status),
            case_insensitive=True,
            max_messages=10_000
        )

        self.data_manager = DataManager()
        self.logger = LogManager()

    async def get_context(self, message, *, cls=ZenContext):
        return await super().get_context(message, cls=cls)

    def load_single_extension(self, folder: str, ext: str) -> NoReturn:
        try:
            self.load_extension(f'zenbot.{folder}.{ext}')
            self.logger.success(f'{ext} was successfully loaded!')
        except Exception as e:
            self.logger.error(f'{ext} cannot be loaded!\n\tError: {e}')

    def startup(self):
        self.logger.debug(f'Bot started at: {str(datetime.now())}')

        self.logger.debug('Removing command: help..')
        self.remove_command('help')

        self.logger.debug('Loading events file..')
        self.load_extension('zenbot.events')

        self.logger.debug('Loading commands..')
        for command in os.listdir('./commands/'):
            self.load_single_extension('commands', command)

        self.logger.debug('Loading plugins..')
        for module in os.listdir('./modules/'):
            self.load_single_extension('modules', module)

        self.logger.debug('Running bot..')
        self.run(config.get('token'))
        self.logger.server('Bot exited!')
