from typing import Set
import Classes.Voice as Voice
import Classes.CleanUp as CleanUp
import Classes.Settings as Settings

def VoiceCommand(tokens: list):
    for key in Settings.get_settings().keys():
        Settings.reset_setting(key)
    
    Voice.TalkVoice("Cleared all settings sir.")

def VoiceAssert(text: str):
    return text.startswith("clear settings")  
    