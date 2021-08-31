import datetime
import Classes.Voice as Voice

def VoiceCommand():
    today = datetime.datetime.today()
    Voice.TalkVoice(
        "Today is " + today.strftime("%A") + " sir."
    )