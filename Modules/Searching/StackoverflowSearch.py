import sys
import json
import requests
from stackapi import StackAPI

if sys.version < '3':
    from urllib2 import urlopen
    from urllib import quote as urlquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote as urlquote

URL = 'https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&q={0}&site=stackoverflow'

class Result:
    def __init__ (self, Title, Tags, Url):
        if len (Title) > 50:
            self.Title = Title[:50] + '...'
        else:
            self.Title = Title

        self.Tags = Tags
        self.Url = Url

def GetJson (_URL):
    Raw = requests.get (_URL, verify = True).text
    JsonData = json.loads (Raw)

    return JsonData

def ParseJson (_Json):
    Results = []

    for Item in _Json['items']:
        Search = Result (str (Item['title']), ', '.join (Item['tags']), str (Item['link']))

        Results.append (Search)

    return Results[0]

def Search (_Search):
    Json = GetJson (URL.format (urlquote (_Search)))

    return ParseJson (Json)
