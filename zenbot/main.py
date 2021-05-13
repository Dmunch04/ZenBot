from .bot import ZenBot


def run():
    bot: ZenBot = ZenBot()
    bot.startup()
