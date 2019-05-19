from fuzzywuzzy import fuzz

class Result:
    def __init__ (self, Word, Definition, SimilarWords):
        self.Word = Word
        self.Definition = Definition
        self.SimilarWords = SimilarWords

def Search (_Word):
    # If the word is not in the dictionary, then do a fuzz with all
    # words in the dict, to find similar words

    pass
