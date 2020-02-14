def GetPrefix (Client, Message):
    # TODO: Check if the server exists in the DB
    if Message.guild is None or Message is None:
        return '!'

    # TODO: Get the specified prefix from the DB
    Prefix = '!'

    return Prefix