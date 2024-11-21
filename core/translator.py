from googletrans import Translator

def translate_text(text, src='auto', dest='en'):
    translator = Translator()
    return translator.translate(text, src=src, dest=dest).text
