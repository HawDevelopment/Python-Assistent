import wikipedia
import Classes.Voice as Voice
import Classes.CleanUp as CleanUp

def VoiceCommand(tokens: list):
    tokens.pop()
    tokens.pop()
    
    text = CleanUp.StringUp(tokens)
    results = wikipedia.summary(text, sentences=1) 
    Voice.TalkVoice("According to Wikipedia", False)
    Voice.TalkVoice(results, False)
    Voice.TalkVoice(", sir.", True)

def VoiceAssert(text: str):
    return "wikipedia" in text or "wikipedia jarvis" in text