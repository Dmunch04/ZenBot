import os
import eve
import json
import shutil

import discord

import Config

def AddServer (_Server : discord.Server):
    Path = Config.Path_Data_Servers + '/' + _Server.id
    User_Path = Path + '/Users'
    Data_Path = Path + '/Data'

    if not os.path.exists (Path):
        os.makedirs (Path)

    if not os.path.exists (User_Path):
        os.makedirs (User_Path)

    if not os.path.exists (Data_Path):
        os.makedirs (Data_Path)

    with open ('Data/Templates/Template_Help.txt', 'r') as File: T_Help = File.read ()
    with open ('Data/Templates/Template_ManagementHelp.txt', 'r') as File: T_MaHelp = File.read ()
    with open ('Data/Templates/Template_MusicHelp.txt', 'r') as File: T_MuHelp = File.read ()
    with open ('Data/Templates/Template_StaffHelp.txt', 'r') as File: T_StHelp = File.read ()
    with open ('Data/Templates/Template_Rules.txt', 'r') as File: T_Rules = File.read ()
    with open ('Data/Templates/Template_Settings.txt', 'r') as File: T_Settings = File.read ()

    with open (Data_Path + '/Help.eve', 'w+') as File: File.write (T_Help)
    with open (Data_Path + '/ManagementHelp.eve', 'w+') as File: File.write (T_MaHelp)
    with open (Data_Path + '/MusicHelp.eve', 'w+') as File: File.write (T_MuHelp)
    with open (Data_Path + '/StaffHelp.eve', 'w+') as File: File.write (T_StHelp)
    with open (Data_Path + '/Rules.eve', 'w+') as File: File.write (T_Rules)
    with open (Data_Path + '/LastTweet.txt', 'w+') as File: File.write ('0')
    with open (Data_Path + '/LastVideo.txt', 'w+') as File: File.write ('0')
    with open (Path + '/settings.eve', 'w+') as File: File.write (T_Settings)

    Data = eve.Load (Path + '/settings.eve')

    NewPath = Data['Path']
    NewPath = NewPath.format (_Server.id).replace ("'", '')

    Data['Path'] = NewPath

    with open (Path + '/settings.eve', 'w') as File:
        File.write (Data)

def RemoveServer (_Server : discord.Server):
    Path = Config.Path_Data_Servers + '/' + _Server.id

    shutil.rmtree (Path)

def UpdateServer (_Before, _After):
    pass

def AddMember (_User : discord.Member):
    Path = Config.Path_Data_Servers + '/' + Server.id + '/Users/' + _User.name + '#' + _User.discriminator + '/' + 'UserFile.eve'

    if not os.path.exists (Path):
        os.makedirs (Path)

    Data = {
        'Name': f'{_User.name}',
        'Tag': f'{_User.discriminator}',
        'ID': f'{_User.id}',
        'Roles': f'{','.join (_User.roles)}',
        'Thanks': 0,
        'Activity': 0,
        'Warnings': 0
    }

    with open (Path, 'w+') as File:
        json.dump (Data, File)

def RemoveMember (_User : discord.User):
    # Fix this here :: Right now it deletes the server folder
    Path = Config.Path_Data_Servers + '/' + Server.id + '/Users/' + _User.name + '#' + _User.discriminator

    shutil.rmtree (Path)

def UpdateMember (_Before, _After):
    pass
