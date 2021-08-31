import json
import random

class Intent:

    def __init__(self, intents, intent_methods={}):
        self.intent_methods = intent_methods

        if intents.endswith(".json"):
            self.load_json_intents(intents)

    def load_json_intents(self, intents):
        self.intents = json.loads(open(intents).read())
    
    def _predict_class(self, message):
        for intent in self.intents['intents']:
            
            if intent['patterns'] != None:
                for pattern in intent['patterns']:
                    if pattern in message:
                        return intent
        return None
    
    def _get_response(self, intent):
        if 'responses' in intent.keys():
            return random.choice(intent['responses'])
    
    def request(self, message, *args):
        intent = self._predict_class(message)
        if intent == None:
            return None
        
        if intent['tag'] in self.intent_methods.keys():
            return self.intent_methods[intent['tag']](*args)
        else:
            return self._get_response(intent)