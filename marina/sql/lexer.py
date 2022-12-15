from sql.tokens import *

# lexer code
class Lexer:
    def __init__(self, string):
        self.string = string
    
    def item(self):
        self.tokens = []
        
        for i in range(len(self.string)):
            # print all data
            if self.string[i] == PRINT:
                self.tokens.append(Token(PRINT))
            
            # inserts certain data
            if self.string[i] == INSERT:
                c = self.string[i+1]
                self.tokens.append(Token(INSERT))
                self.tokens.append(self.string[i+2:])
                print(self.tokens)
                
            if self.string[i] == REMOVE:
                c = self.string[i+1]
                self.tokens.append(Token(REMOVE))
                self.tokens.append(self.string[i+1:])
                
            if self.string[i] == SEARCH:
                c = self.string[i+1]
                self.tokens.append(Token(SEARCH))
                self.tokens.append(self.string[i+2:])
                
        return list(self.tokens)