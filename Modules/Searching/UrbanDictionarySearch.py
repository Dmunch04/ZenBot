import urbandictionary

class Result:
    def __init__ (self, Word, Definition, Example, Upvotes, Downvotes):
        self.Word = Word
        self.Definition = Definition
        self.Example = Example
        self.Upvotes = Upvotes
        self.Downvotes = Downvotes

def Search (_Search):
    Definition = urbandictionary.define (_Search)[0]

    return Result (Definition.word, Definition.definition, Definition.example, Definition.upvotes, Definition.downvotes)
