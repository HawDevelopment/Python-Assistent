import Classes.Voice as Voice
import Classes.Lexer as Lexer
import Classes.Parser as Parser
import Extension
from Classes.CleanUp import CleanUp, StringUp

from nltk.util import pr
import os

START_COMMAND = 'hey jarvis'

for file in os.listdir('./Commands'):
    if file != "__pycache__":
        Extension.load_command(file)

while True:
    #text = Voice.TakeVoice().lower()
    text = input("> ").lower()
    
    if text == "exit":
        break
    
    if text.count(START_COMMAND) > 0:
        
        text = CleanUp(text[text.find(START_COMMAND):])
        tokens = Lexer.run(text)
        parsed, error = Parser.run(tokens)
        
        if not error and parsed != None and parsed['Command'] != None:
            #network.request(StringUp(parsed['Command'].tokens))
            
            # Execute command
        else:
            Voice.TalkVoice('', True, True)
            
            response_command = Voice.TakeVoice()
            if response_command == None or response_command == "":
                Voice.TalkVoice('I did not understand you, sir.', True)
                continue
            
            text = CleanUp(response_command)
            tokens = Lexer.run(text)
            parsed, error = Parser.run(tokens)
            text = StringUp(parsed['Command'].tokens)
            
            #result = network.request(text)
            if result == "DidntUnderstand":
                
                for module in Extension.get_modules():
                    if hasattr(module, 'VoiceAssert') and getattr(module, 'VoiceAssert')(text):
                        getattr(module, 'VoiceCommand')(parsed['Command'].tokens)
                        break
                
    
    #if error:
    #    Voice.TalkVoice('There was an error')
    #    print(error)

#Voice.TalkVoice(say_time=True)
#Voice.TalkVoice("A bit cringe init bruv not gonna lie", say_time=True)

#Voice.TalkVoice("We call these chips, instead of", run_and_wait=False)
#Voice.TalkVoice("Krispity Crunchy Munchy Crapjack Snaping Niblers Snaping Crackpop Queen's lovely joelly delites. Thats rather cringe init bruv")
