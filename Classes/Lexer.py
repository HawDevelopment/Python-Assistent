
#
# TOKEN
#

TOKEN_TYPES = {
    'n': 'NOUN',
    'v': 'VERB',
    'a': 'ADJECTIVE',
    's': 'ADJECTIVE',
    'r': 'ADVERB',
    'pr': 'PRONOUN',
    'p': 'PUNCTUATION',
    'uw': 'UNKNOWN_WORD',
    'ut': 'UNKNOWN_TYPE',
}

PUNCTUATION_TYPES = ".?!,:;- \"\' []\{\}() ..." 
PRONOUN = "it it's its you i he they we she who them me him one her us something nothing anything himself everything someone themselves everyone itself anyone myself"

class Token:
    def __init__(self, type, value):
        self.type = type
        self.word = value
    
    def __str__(self):
        return 'Token{0}({1})'.format(self.type, self.word)
    
    def __repr__(self) -> str:
        return self.__str__()

#
# LEXER
#

#import nltk
#nltk.download('wordnet')

from nltk.corpus import wordnet
from nltk.tokenize import TweetTokenizer
from nltk.util import pr

Tokenizer = TweetTokenizer()

class Lexer:
    def __init__(self, text):
        self.text = text if type(text) is list else Tokenizer.tokenize(text)
        self.pos = 0
        self.current_word = self.text[self.pos]
    
    def __iter__(self):
        return self.text
    
    def advance(self):
        self.pos += 1
        self.current_word = self.text[self.pos] if self.pos < len(self.text) else None
        
    def get_type(self, synsets):
        for synset in synsets:
            if synset.name().split(".")[0] == self.current_word.lower():
                return synset.pos()
    
    def tokenize(self):
        tokens = []
        
        while self.current_word != None:
            if self.current_word in PUNCTUATION_TYPES:
                tokens.append(Token(TOKEN_TYPES['p'], self.current_word))
            elif self.current_word.lower() in PRONOUN:
                tokens.append(Token(TOKEN_TYPES['pr'], self.current_word))
            else:
                synsets = wordnet.synsets(self.current_word)
                word_type = self.get_type(synsets)
                                
                if word_type == None:
                    tokens.append(Token('UNKNOWN_WORD', self.current_word))
                elif TOKEN_TYPES.get(word_type) == None:
                    tokens.append(Token('UNKNOWN_TYPE', self.current_word))
                else:
                    tokens.append(Token(TOKEN_TYPES[word_type], self.current_word))
            
            self.advance()
        
        return tokens

def run(text: str = ""):
    lexer = Lexer(text)
    tokens = lexer.tokenize()
    return tokens