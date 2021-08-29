
from nltk.util import pr


class Error:
    def __init__(self, message = "An Error occured", details = "UnExpected", serverity = "error") -> None:
        self.message = message
        self.details = details
        self.level = serverity
    
    def to_string(self):
        return "{0} {1}: {2}".format(self.details, self.level, self.message)
    
    def __str__(self) -> str:
        return self.to_string()
    
    def __repr__(self) -> str:
        return self.to_string()

class ParserError(Error):
    def __init__(self, message = "", serverity = "error") -> None:
        return super().__init__(message, "Parser", serverity)