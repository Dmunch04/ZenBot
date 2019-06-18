import re

def FindURL (_String: str):
    """
        Finds urls in a string, and returns them.
        It also returns the other contents of the string, but splitted.

        Source: https://www.geeksforgeeks.org/python-check-url-string/
    """

    URLS = re.findall ('[http[s]?://]|[www.](?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', _String)

    Text = _String

    for URL in URLS:
        Text = Text.replace (URL, '')

    return Text, URLS[0]
