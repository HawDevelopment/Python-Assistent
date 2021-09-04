import Classes.Lexer as Lexer
import Classes.Parser as Parser

un_needed_words = ["please"]
un_needed_sentence = ["can you"]

def CleanUp(text: str):
    for sentence in un_needed_sentence:
        text = text.replace(sentence, "")
    
    split = text.split()
    return ' '.join([x for x in split if x.lower() not in un_needed_words])

def StringUp(tokens):
    text = []
    for token in tokens:
        if isinstance(token, list):
            text.append(StringUp(token))
            continue
        
        if token.type == Lexer.TOKEN_TYPES['p']:
            text.append("\b" + token.word)
        else:
            text.append(token.word)
    
    return ' '.join(text)