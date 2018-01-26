from typing import List
from compiler.scanner.token import Token


class Scanner:
    def __init__(self, source_file: str=""):
        """
        Default constructor, initializes token sequence and stores desired source file string

        :param source_file: str referencing the location of a file to be analyzed
        """
        self.sequence = List[Token]
        self.file = source_file
