import webbrowser as web
import Classes.Voice as Voice
import Classes.CleanUp as CleanUp

def VoiceCommand(tokens: list):
    if tokens[0].word == 'search' or tokens[0].word == 'open':
        tokens.pop(0)
    
    if tokens[len(tokens) - 1].word == "jarvis":
        tokens.pop()
    
    
    text = CleanUp.StringUp(tokens)
    text = text.replace("on google", "")
    
    results = web.open("https://www.google.com/search?q="+text) 
    Voice.TalkVoice("Searched, " + text + " on google, sir.", False)

def VoiceAssert(text: str):
    return (text.startswith("search") or text.startswith("open")) and (text.endswith("on google") or text.endswith("on google jarvis"))