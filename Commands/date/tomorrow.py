import datetime
import Classes.Voice as Voice

def VoiceCommand():
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    Voice.TalkVoice(
        "Tomorrow is " + str(tomorrow.day) + " sir."
    )