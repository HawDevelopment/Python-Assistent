import Classes.Voice as Voice
import Classes.CleanUp as CleanUp
import Classes.Settings as Settings

def VoiceCommand(tokens: list):
    text = CleanUp.StringUp(tokens)
    text = text.replace("set", "").replace("setting", "")
    text = text.strip()
    
    split = text.split("to")
    try:
        Settings.set_setting(split[0], split[1])
    except IndexError:
        return Voice.TalkVoice("No value given sir.")
    
    Voice.TalkVoice("The value of " + split[0] + " is now " + split[1] + " sir.")

def VoiceAssert(text: str):
    return text.startswith("set") and "to" in text  
    