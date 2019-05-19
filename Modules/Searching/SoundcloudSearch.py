import soundcloud

Client = soundcloud.Client (client_id = '175c043157ffae2c6d5fed16c3d95a4c')

class Result:
    def __init__ (self, Title, Author, Url):
        self.Title = Title
        self.Author = Author
        self.Url = Url

def Search (_Search):
    Song = Client.get ('/tracks', q = _Search)[0]

    return Result (Song.title, Song.id, Song.id) # Change to Author and Url

a = Search ('dj spotify')
print (a.Url)
