class Token:
    def __init__(self, line: int=0, column: int=0, lexeme: str="", string: str=""):
        self.line = line
        self.column = column
        self.lexeme = lexeme
        self.string = string
