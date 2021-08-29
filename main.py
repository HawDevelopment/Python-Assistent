from nltk.util import pr
import Classes.Voice as Voice
import Classes.Lexer as Lexer
import Classes.Parser as Parser
from Classes.CleanUp import CleanUp, StringUp

from neuralintents import GenericAssistant

START_COMMAND = 'hey jarvis'

def greeting():
    Voice.TalkVoice('Im doing great, sir.')

network = GenericAssistant("Commands.json", intent_methods={
    'status': greeting
})

#network.train_model()
#network.save_model()

network.load_model()

while True:
    text = Voice.TakeVoice().lower()
    if text == "exit":
        break
    
    if text.count("hey jarvis") > 0:
        
        text = CleanUp(text[text.find(START_COMMAND):])
        tokens = Lexer.run(text)
        parsed, error = Parser.run(tokens)
        
        if not error and parsed != None and parsed['Command'] != None:
            network.request(StringUp(parsed['Command'].tokens))
            
            # Execute command
        else:
            Voice.TalkVoice('Hi sir.', True, True)
            
            response_command = Voice.TakeVoice()
            if response_command == None or response_command == "":
                Voice.TalkVoice('I did not understand you, sir.', True)
                continue
            
            network.request(response_command)
    
    #if error:
    #    Voice.TalkVoice('There was an error')
    #    print(error)

#Voice.TalkVoice(say_time=True)
#Voice.TalkVoice("A bit cringe init bruv not gonna lie", say_time=True)

#Voice.TalkVoice("We call these chips, instead of", run_and_wait=False)
#Voice.TalkVoice("Krispity Crunchy Munchy Crapjack Snaping Niblers Snaping Crackpop Queen's lovely joelly delites. Thats rather cringe init bruv")
