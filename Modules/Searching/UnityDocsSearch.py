import sys
import json

if sys.version < '3':
    from urllib2 import urlopen
    from urllib import quote as urlquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote as urlquote

#import Config

class Result:
    def __init__ (self, Title, Description, Url):
        self.Title = Title

        if len (Description) > 50:
            self.Description = Description[:50] + '...'
        else:
            self.Description = Description

        self.Url = Url

def GetJson (_Docs):
    if _Docs == 'script':
        JsonData = json.loads (urlopen (Config.Url_Unity_Script).read ())

        #Config.Path_Data_Unity_API
        #with open ('../../Data/UnityDocs/Script.json', 'r') as File:
            #JsonData = json.loads (File.read ())
    else:
        JsonData = json.loads (urlopen (Config.Url_Unity_Manual).read ())

        #Config.Path_Data_Unity_Manual
        #with open ('../../Data/UnityDocs/Manual.json', 'r') as File:
            #JsonData = json.loads (File.read ())

    return JsonData

def ParseJson (_Search, _Json):
    Results = []

    for Element in _Json:
        if _Search in Element['title']:
            Item = Result (str (Element['title']), str (Element['description']), str (Element['link']))
            Results.append (Item)

    return Results[0]

def Search (_Search, _Docs):
    Json = GetJson (_Docs)

    return ParseJson (_Search, Json)
