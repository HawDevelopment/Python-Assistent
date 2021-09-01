import webbrowser as web
from Classes.CleanUp import StringUp

def VoiceCommand(tokens):
    tokens.pop(0)
    
    web.open("www." + tokens[0].word + ".com")

def VoiceAssert(text: str):
    return text.startswith('open') and not (text.endswith('on google') or text.endswith('on google jarvis'))