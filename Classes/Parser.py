
#
# NODE and NODETYPES and NODERESULT
#

from nltk.util import pr
import Classes.Lexer as Lexer
from Classes.Error import *

SENTENCE_START = 'hello hi godday godevening godmorning hey'
SENTENCE_END = '.?!'

class WordNode():
    def __init__(self, token):
        self.token = token
    
    def __str__(self) -> str:
        return 'WordNode({0})'.format(self.token)
    
    def __repr__(self) -> str:
        return self.__str__()

class StatementNode:
    def __init__(self, *tokens):
        self.tokens = tokens
    
    def __str__(self) -> str:
        return 'StatementNode[{0}]'.format(str(self.tokens))
    
    def __repr__(self) -> str:
        return self.__str__()
    
class ParserResult:
    def __init__(self, node = None, error = None) -> None:
        self.node = node
        self.error = error
        
    def __repr__(self) -> str:
        return self.Eval().__repr__()
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def Succes(node: any):
        return ParserResult(node, None)
    
    def Error(error: ParserError):
        return ParserResult(None, error)
    
    def NotFound():
        return ParserResult()
    
    def Import(res):
        return res.node, res
        
    def Eval(self):
        if isinstance(self.error, Error):
            return self.error
        else:
            return self.node
    
    def is_error(self):
        return self.error is not None and isinstance(self.error, ParserError)
    
    def is_level(self, level):
        return self.is_error() and self.error.level == level
        

class ParserTypes:
    def Start(parser):
        token = parser.current_token
        next_token = parser.advance()
        types = (Lexer.TOKEN_TYPES['n'], Lexer.TOKEN_TYPES['uw'], Lexer.TOKEN_TYPES['n'])
        
        if not next_token:
            return ParserResult.Error(ParserError("Not enough tokens!", 'warn'))
        
        if (token.word.lower() or next_token.word.lower()) not in SENTENCE_START:
            return ParserResult.Error(ParserError("Expected a sentence!", 'warn'))
        
        if (token.type and next_token.type) not in types:
            return ParserResult.Error(ParserError("Expected word to be in start!", 'error'))
        
        if parser.next() and parser.next().type == Lexer.TOKEN_TYPES['p']:
            parser.advance()
        
        parser.advance()
        return ParserResult.Succes(StatementNode(token, next_token))
    
    def Command(parser):
        if parser.current_token == None:
            return ParserResult.NotFound()
        
        statement = []
        while parser.current_token != None and parser.current_token.word not in SENTENCE_END:
            statement.append(parser.current_token)
            parser.advance()
        
        parser.advance()
        return ParserResult.Succes(StatementNode(*statement)) if len(statement) > 0 else ParserResult.Error(ParserError("Expected a command!", 'error'))
        

#
# Parser
#

commands = {
    'Start': ParserTypes.Start,
    'Command': ParserTypes.Command,
}

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = -1
        self.advance()
    
    def advance(self):
        self.index += 1
        self.current_token = self.tokens[self.index] if self.index < len(self.tokens) else None
        return self.current_token
    
    def next(self):
        index = self.index + 1
        return self.tokens[index] if index < len(self.tokens) else None
        
    def run(self):
        
        if len(self.tokens) == 0:
            return None, ParserError("No tokens!")
        
        ret = {}
        for index, func in commands.items():
            if self.current_token == None:
                break
            
            result = func(self)
            if result.is_level('error'):
                return None, result.Eval()
            elif result.is_error():
                continue
            
            ret[index] = result.Eval()
        
        if len(ret) == 0:
            return None, ParserError('No output!')
        
        return ret, None

def run(tokens):
    parser = Parser(tokens)
    return parser.run()