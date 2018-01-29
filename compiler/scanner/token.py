class Token:
    def __init__(self, line: int=0, column: int=0, token: str="", lexeme: str=""):
        self.line = line
        self.column = column
        self.token = token
        self.lexeme = lexeme
