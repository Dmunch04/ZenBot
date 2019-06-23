import os
import json

def GetPrefix (_Client, _Message):
    if _Message.guild is None or not os.path.isdir (f'Data/Servers/{_Message.guild.id}'):
        return '!'

    with open (f'Data/Servers/{_Message.guild.id}/Server.json', 'r') as ServerFile:
        Data = json.loads (ServerFile.read ())

    Prefix = Data['Prefix']

    return Prefix
