import speech_recognition as sr
import pyttsx3
from Classes.TimeOfDay import TimeOfDay
import Classes.Settings as Settings

r = sr.Recognizer()
m = sr.Microphone()
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[Settings.get_setting("voice id")].id)
engine.setProperty('rate', Settings.get_setting("voice rate"))

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(
#        index, name))

with m as source:
    r.adjust_for_ambient_noise(source)

def TakeVoice():
    global r
    recognized_text = ""
    with m as source:
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Timeout")
            return ""
        
        try:
            recognized_text = r.recognize_google(audio)
        except sr.UnknownValueError:
            r = sr.Recognizer()
        except sr.RequestError as e:
            print("Could not request: {0}".format(e))
        
    return recognized_text

def TalkVoice(text: str = "There was an error, sir.", run_and_wait: bool = True, say_time: bool = False):
    
    if say_time:
        engine.say(TimeOfDay())
    
    engine.say(text)
    if run_and_wait == True:
        engine.runAndWait()
        