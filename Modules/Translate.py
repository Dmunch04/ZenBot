import googletrans

def Translate (_Text, _From = 'en', _To = 'en'):
    Translator = googletrans.Translator ()

    try:
        Translation = Translator.translate (_Text, src = _From, dest = _To)
        return Translation

    except:
        return 'Error'
