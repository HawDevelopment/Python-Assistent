import datetime
import Classes.Voice as Voice

def VoiceCommand():
    today = datetime.datetime.now()
    Voice.TakeVoice(
        "Current week number is " + today.strftime("%U") + " sir."
    )