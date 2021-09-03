import Classes.Voice as Voice
import Classes.CleanUp as CleanUp
import Classes.Settings as Settings

def VoiceCommand(tokens: list):
    text = CleanUp.StringUp(tokens)
    text = text.replace("reset", "").replace("setting", "")
    text = text.strip()
    
    try:
        Settings.reset_setting(text)
    except Exception:
        return Voice.TalkVoice()
    
    Voice.TalkVoice("The value of " + text + " is now " + str(Settings.get_setting(text)) + " sir.")

def VoiceAssert(text: str):
    return text.startswith("reset")  
    