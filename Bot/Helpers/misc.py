import os, json

def get_prefix(bot, message):
    if message.guild is None:
        return "!"
    
    if not os.path.isdir(f'Data/Servers/{message.guild.id}'):
        return "!"

    with open(f'Data/Servers/{message.guild.id}/Server.json', 'r') as f:
        data = json.load(f)

    prefix = data["Prefix"]
    return(prefix)