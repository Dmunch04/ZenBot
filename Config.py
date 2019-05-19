# TODO: CREATE A BETTER STRUCTURE AND BETTER COMMENTS!

# Package Imports
import os

# Bot Token. If you're hosting this yourself, make sure
# to replace this with your token.
Token = 'key'

# The bots command prefix
Prefix = '!'

# API keys (Remove on release)
#Key_Youtube = os.environ ['Key_Youtube']
Key_Youtube = 'key'
API_Twitter = 'key'
API_Secret_Twitter = 'key'
Access_Twitter = 'key'
Access_Secret_Twitter = 'key'

# Paths
# General paths
Path_Data = 'Data'
Path_Data_Info = Path_Data + '/Info.eve'
Path_Data_Servers = Path_Data + '/Servers'
# Unity paths
Path_Unity_Docs = Path_Data + '/UnityDocs'
Path_Data_Unity_Manual = Path_Unity_Docs + '/Manual.json'
Path_Data_Unity_API = Path_Unity_Docs + '/Script.json'

# URLS
Url_Unity_Script = 'http://munchii.me/unitydocs/script.json'
Url_Unity_Manual = 'http://munchii.me/unitydocs/manual.json'

# Errors
Errors = {
    'Specify': {
        'Title': 'Specify Search',
        'Type': 'Command Error',
        'Error': 'Please specify what you wanna search for!',
        'Code': '76.XE001'
    },

    'Permission': {
        'Title': 'No Permission',
        'Type': 'Permission Error',
        'Error': "Looks like you don't have the permission for that command!",
        'Code': '76.XE002'
    },

    'Result': {
        'Title': 'No Result',
        'Type': 'Search Error',
        'Error': "Looks like we couldn't find what you searched for!",
        'Code': '76.XE003'
    },

    'Unkown': {
        'Title': 'Something went wrong..',
        'Type': 'Error',
        'Error': 'Whoops! Looks like something went wrong.',
        'Code': '76.XE004'
    }
}

# Commands Data
Commands_Folder = 'Commands'
# A list of the commands. Remove or comment out the ones you don't wanna use
Commands = [
    'Default.About',
    'Default.Dictionary'
    'Default.Help',
    'Default.Role',
    'Default.Rule',
    'Default.Server',
    'Default.Support',
    'Default.Translate',
    'Default.User',
    'Search.Google',
    'Search.Wikipedia',
    'Search.Youtube',
    'Search.YoutubeChannel',
    'Search.TwitchChannel',
    'Search.UnityDocs',
    'Search.UrbanDictionary',
    'Search.Stackoverflow',
    'Search.Soundcloud',
    'Staff.Ban',
    'Staff.Kick',
    'Staff.Mute',
    'Staff.Warn',
    'Staff.Update',
    'Staff.Management'
]

# Addons :: This will get updates from twitter and youtube and post them
# Remove or comment them out if you don't want it
Addons = [
    'TwitterGetter',
    'YoutubeGetter'
]
