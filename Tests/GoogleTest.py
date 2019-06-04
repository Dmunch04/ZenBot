from googlesearch.googlesearch import GoogleSearch

def Search (_Word):
    Result = GoogleSearch ().search (_Word)

    return Result[0]

Search ('hello')
