import googletrans

def Translate (_Text, _From = 'en', _To = 'en'):
    Translator = googletrans.Translator ()

    try:
        Translation = Translator.translate (_Text, src = _From, dest = _To)
        return Translation.text

    except:
        return 'Error'

Result = Translate ('Hello, World!', 'en', 'da')
print (Result)

# Test Result:
# Print :: Hej Verden!
# Status: Completed / Working
