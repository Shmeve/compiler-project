from compiler.scanner.token import Token
from compiler.scanner.transition_table import TransitionTable
from compiler.tools import regular_expressions as RE
from compiler.tools import constants


class Scanner:
    def __init__(self, source_file: str="compiler/samples/sample_1"):
        """
        Default constructor, initializes token sequence and stores desired source file string.

        :param source_file: str referencing the location of a file to be analyzed
        """
        self.table: TransitionTable = TransitionTable()
        self.current_state: int = 1
        self.sequence: list = []
        self.file: list = []
        self.line_number: int = 0
        self.char_position: int = -1

        # Setup state transition table
        self.table.build_table()
        self.table.build_state_token_list()

        # Read file contents
        with open(source_file, 'r') as f:
            self.file = f.readlines()

    def next_token(self) -> Token:
        """
        Scans file until a final state is reached, at which point the correct token for the processed portion of code is
        returned.

        :return: Token
        """
        self.current_state = 1
        token = Token(self.line_number, self.char_position)
        token_found = False

        while not token_found:
            read_char = self.next_char()
            transition = self.input_to_transition_table_key(read_char)
            self.current_state = self.table.get_state(self.current_state, transition)

            if self.table.is_final_state(self.current_state):
                token_found = True
                token.lexeme = self.lookup_token(self.current_state, token.string)

                if read_char is not "\n":
                    self.backup_char()
            else:
                token.string += read_char

        return token

    def next_char(self) -> str:
        """
        Returns the next character from file.

        :return: str
        """
        if self.char_position is not -1 and self.file[self.line_number][self.char_position] is '\n':
            self.line_number += 1
            self.char_position = 0
        else:
            self.char_position += 1

        return self.file[self.line_number][self.char_position]

    def backup_char(self) -> str:
        """
        Returns previous character from file.

        :return: str
        """
        if self.char_position is 0 and self.line_number is not 0:
            self.line_number -= 1
            self.char_position = len(self.file[self.line_number]) - 1
        elif self.char_position is not -1:
            self.char_position -= 1

        return self.file[self.line_number][self.char_position]

    def current_char(self) -> str:
        """
        Returns the character currently being analyzed by the scanner

        :return: str
        """
        return self.file[self.line_number][self.char_position]

    def lookup_token(self, state: int, string: str="") -> str:
        """
        Look up the token for the specified final state.

        :param state: a final state
        :param string: string that lead to current state
        :return: str
        """
        token = self.table.state_token[state]

        if token is constants.T_A_ID and string in constants.RESERVED_IDS.keys():
            return constants.RESERVED_IDS[string]

        return self.table.state_token[state]

    def input_to_transition_table_key(self, input_char: str) -> str:
        """
        Converts the given input character to the correct key for the state transition table based on a series of
        regular expressions denoted by the languages grammar.

        :param input_char: Character to convert
        :return: str
        """
        if RE.l_e(input_char):
            return "non_e"

        if RE.e(input_char):
            return "e"

        if RE.d_0(input_char):
            return "non_zero"

        if RE.zero(input_char):
            return "0"

        if RE.eol(input_char):
            return "EOL"

        if RE.eof(input_char):
            return "EOF"

        return input_char   # Read as is (special reserved character)
