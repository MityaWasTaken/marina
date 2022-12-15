# commands
PRINT = 'P'
INSERT = 'I'
REMOVE = 'R'
SEARCH = 'S'

# token object
class Token:
    def __init__(self, value=None):
        self.value = value
    def __repr__(self):
        if self.value: return repr(self.value)
        raise Exception("value got messed up")
    