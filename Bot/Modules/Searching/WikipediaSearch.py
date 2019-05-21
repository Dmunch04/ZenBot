import wikipedia

class Result:
    def __init__ (self, Title, Content, Url):
        if len (Title) > 50:
            self.Title = Title[:50] + '...'
        else:
            self.Title = Title

        if len (Content) > 50:
            self.Content = Content[:50] + '...'
        else:
            self.Content = Content

        self.Url = Url

def Search (_Search):
    Item = wikipedia.page (_Search)

    return Result (Item.title, Item.content, Item.url)
