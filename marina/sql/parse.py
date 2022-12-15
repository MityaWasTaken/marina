import sql.lexer as l
from sql.tokens import *

# parser code for deciding what to do
def Parser(string):
    tk = l.Lexer(string)
    tk = tk.item()
    
    if str(tk[0])[1] == INSERT:
        return str(tk[1]).upper()
        
    elif str(tk[0])[1] == PRINT:
        return "P"
    
    elif str(tk[0])[1] == REMOVE:
        return str(tk[1]).lower()
    
    elif str(tk[0])[1] == SEARCH:
        return str(tk[1]).title()
    
    return