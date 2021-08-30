import datetime
import Classes.Voice as Voice

def VoiceCommand():
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    Voice.TakeVoice(
        "Tomorrow is " + tomorrow.day + " sir."
    )