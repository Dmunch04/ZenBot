import json
from fuzzywuzzy import fuzz

DiffMin = 95
DiffMinCompare = 80

def FindWord (_Word):
    with open ('Dictionary.json', 'r') as File:
        Data = json.loads (File.read ())

    Word = _Word.lower ()

    for xWord in Data:
        Difference = fuzz.ratio (Word, xWord)

        if Difference >= DiffMin:
            return True

    return False

def Search (_Word):
    Result = FindWord (_Word)

    with open ('Dictionary.json', 'r') as File:
        Data = json.loads (File.read ())

    if Result:
        return _Word

    else:
        CloseWords = []

        for Word in Data:
            Difference = fuzz.ratio (_Word, Word)
            if Difference >= DiffMinCompare and len (CloseWords) < 10:
                CloseWords.append (Word)

        return CloseWords

Test = Search ('Spottedd')
print (Test)

# Test Result:
# Print :: ['spottedd']
# Status: Completed / Working
