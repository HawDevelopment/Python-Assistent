from typing import Text
import wikipedia
import Classes.Voice as Voice
import Classes.CleanUp as CleanUp

def VoiceCommand(tokens: list):
    tokens.pop()
    tokens.pop()
    
    text = CleanUp.StringUp(tokens)
    results = wikipedia.summary(text, sentences=5) 
    Voice.TalkVoice("According to Wikipedia", False)
    Voice.TalkVoice(results, False)
    Voice.TakeVoice(", sir.", True)

def VoiceAssert(text: str):
    return text.endswith("wikipedia") or text.endswith("wikipedia jarvis")