import sys
import json
import requests

if sys.version < '3':
    from urllib2 import urlopen
    from urllib import quote as urlquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote as urlquote

URL = ''

class Channel:
    def __init__ (self, Name, Subs, Videos, Url):
        self.Name = Name
        self.Subs = Subs
        self.Videos = Videos
        self.Url = Url

class Video:
    def __init__ (self, Title, Description, Url):
        self.Title = Title
        self.Description = Description
        self.Url = Url

def GetJson (_URL):
    JsonData = ''

    return JsonData

def ParseJson (_URL, _Type):
    Results = []

    return Results[0]

def SearchChannel (_Search):
    Json = GetJson (URL.format (urlquote (_Search)))

    return ParseJson (Json, 'Channel')

def SearchVideo (_Search):
    Json = GetJson (URL.format (urlquote (_Search)))

    return ParseJson (Json, 'Video')
