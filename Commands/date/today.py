import datetime
import Classes.Voice as Voice

def VoiceCommand():
    today = datetime.datetime.today()
    Voice.TakeVoice(
        "Today is " + today.day + " sir."
    )