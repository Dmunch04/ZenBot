import eve

import discord

import Config

def CheckCommand (_Command, _ServerID):
    Path = Config.Path_Data_Servers + '/' + _ServerID + '/settings.eve'

    Command = 'Command_' + _Command

    Data = eve.load (Path)

    Enabled = False

    for Item in Data:
        if Item == Command:
            Enabled = Data[Item]

    return Enabled
