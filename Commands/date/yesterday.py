import datetime
import Classes.Voice as Voice

def VoiceCommand():
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    Voice.TalkVoice(
        "Yesterday was " + str(yesterday.day) + " sir."
    )