from typing import Set
import Classes.Voice as Voice
import Classes.CleanUp as CleanUp
import Classes.Settings as Settings

def VoiceCommand(tokens: list):
    text = CleanUp.StringUp(tokens)
    text = text.replace("reset", "").replace("setting", "")
    text = text.strip()
    
    try:
        Settings.reset_setting(text)
    except IndexError:
        return Voice.TalkVoice("No setting with that name sir.")
    
    Voice.TalkVoice("The value of " + text + " is now " + Settings.get_setting(text) + " sir.")

def VoiceAssert(text: str):
    return text.startswith("reset")  
    