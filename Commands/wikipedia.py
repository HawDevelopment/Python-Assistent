import wikipedia
import Classes.Voice as Voice
import Classes.CleanUp as CleanUp

def VoiceCommand(tokens: list):
    if tokens[0].word == 'what' and tokens[1].word == 'is':
        tokens.pop(0)
        tokens.pop(0)
    
    if tokens[len(tokens) - 1].word == "jarvis":
        tokens.pop()
    
    text = CleanUp.StringUp(tokens)
    text = text.replace("on wikipedia", "")
    
    results = wikipedia.summary(text, sentences=1) 
    Voice.TalkVoice("According to Wikipedia", False)
    Voice.TalkVoice(results, False)
    Voice.TalkVoice(" sir.", True)

def VoiceAssert(text: str):
    if text.startswith("what is"):
        return True
    elif text.endswith("on wikipedia") or text.endswith("on wikipedia jarvis"):
        return True
    return False