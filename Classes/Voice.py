from nltk.util import pr
import speech_recognition as sr
import pyttsx3
from Classes.TimeOfDay import TimeOfDay

r = sr.Recognizer()
m = sr.Microphone()
engine = pyttsx3.init('sapi5')

# Should use settings
voices = engine.getProperty('voices')

if voices[2] != None and voices[2].id == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_GeorgeM":
    engine.setProperty('voice', voices[2].id) # 2 is george
else:
    engine.setProperty('voice', voices[0].id)

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(
#        index, name))

with m as source:
    r.adjust_for_ambient_noise(source)

def TakeVoice():
    recognized_text = ""
    with m as source:
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7.5)
        except sr.WaitTimeoutError:
            print("Timeout")
            return ""
        
        try:
            recognized_text = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Unkown value error!")
        except sr.RequestError as e:
            print("Could not request: {0}".format(e))
        
    return recognized_text

def TalkVoice(text: str = "There was an error, sir.", run_and_wait: bool = True, say_time: bool = False):
    
    if say_time:
        engine.say(TimeOfDay())
    
    engine.say(text)
    if run_and_wait == True:
        engine.runAndWait()
        