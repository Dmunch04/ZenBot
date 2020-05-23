from .bot import ZenBot


def run():
    instance: ZenBot = ZenBot()
    instance.startup()
    #instance.run("")