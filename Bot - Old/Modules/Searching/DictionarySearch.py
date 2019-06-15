import json
from fuzzywuzzy import fuzz

class Result:
    def __init__ (self, Word, Definition, SimilarWords = []):
        self.Word = Word
        self.Definition = Definition
        self.SimilarWords = SimilarWords

DiffMin = 95
DiffMinCompare = 80

def FindWord (_Word, _Data):
    Word = _Word.lower ()

    for xWord in _Data:
        Difference = fuzz.ratio (Word, xWord)

        if Difference >= DiffMin:
            return True

    return False

def Search (_Word):
    with open ('../../Data/Dictionary.json', 'r') as File:
        Data = json.loads (File.read ())

    Result = FindWord (_Word, Data)

    if Result:
        #return _Word
        return Result (_Word, Data[_Word], [])

    else:
        CloseWords = []

        for Word in Data:
            Difference = fuzz.ratio (_Word, Word)
            if Difference >= DiffMinCompare and len (CloseWords) < 10:
                CloseWords.append (Word)

        return CloseWords
