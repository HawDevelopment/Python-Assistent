import Classes.Voice as Voice
import Classes.Lexer as Lexer
import Classes.Parser as Parser
import Classes.Settings as Settings
import Extension
from Classes.CleanUp import CleanUp, StringUp

#from nltk.util import pr
import os
from Intents import Intent


START_COMMAND = 'hey jarvis'

for file in os.listdir('./Commands'):
    if file != "__pycache__":
        Extension.load_command(file)

intent = Intent("Commands.json", Extension.get_commands())

print("Taking input!")
while True:
    try:
        if Settings.get_setting('voice') == True:
            text = Voice.TakeVoice().lower()
        else:
            text = input("> ").lower()
        
        if len(text) > 0:
            print(text)
    except KeyboardInterrupt:
        break
    
    if text == "exit":
        break
    
    if text.count(START_COMMAND) > 0:
        
        text = CleanUp(text[text.find(START_COMMAND):])
        tokens = Lexer.run(text)
        parsed, error = Parser.run(tokens)
        
        response_question = None
        if error == None and parsed != None and parsed.get('Command') != None:
            response_question = StringUp(parsed['Command'])
        else:
            Voice.TalkVoice('', True, True)
            
            response_command = Voice.TakeVoice()
            if response_command == None or response_command == "":
                Voice.TalkVoice('I did not understand you, sir.', True)
                continue
            
            text = CleanUp(response_command)
            tokens = Lexer.run(text)
            parsed, error = Parser.run(tokens)
            response_command = StringUp(parsed['Command'])
        
        
        result = intent.request(response_question)
        if result == None:
            for name, module in Extension.get_modules().items():
                if hasattr(module, 'VoiceAssert') and getattr(module, 'VoiceAssert')(response_question) == True:
                    Extension.get_commands()[name]([*parsed['Command']])
                    break
                
    
    #if error:
    #    Voice.TalkVoice('There was an error')
    #    print(error)

Settings.save_settings()

#Voice.TalkVoice(say_time=True)
#Voice.TalkVoice("A bit cringe init bruv not gonna lie", say_time=True)

#Voice.TalkVoice("We call these chips, instead of", run_and_wait=False)
#Voice.TalkVoice("Krispity Crunchy Munchy Crapjack Snaping Niblers Snaping Crackpop Queen's lovely joelly delites. Thats rather cringe init bruv")
