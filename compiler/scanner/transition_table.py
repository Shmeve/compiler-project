from compiler.tools import constants
from collections import OrderedDict
import csv


class TransitionTable:
    def __init__(self, csv_path: str="compiler/tools/state_transition_table.csv"):
        """
        Constructor for TransitionTable object.

        :param csv_path: str, location of csv file to use when constructing the state transition table.
        """
        self.csv_path: str = csv_path
        self.table: list = []
        self.state_token: list = []

        # Generate list of empty strings for each state
        for i in range(61):
            self.state_token.append("")

    def build_table(self) -> None:
        """
        Create state transition table from CSV. The table is represented as a List of Dictionaries where the state
        to transition to can be accessed via table[currentState: int][inputKey: str].

        :return: None
        """
        with open(self.csv_path, newline='') as csvfile:
            lines = list(csv.reader(csvfile, delimiter=',', quotechar='"'))

        keys = lines[0]
        self.table.append(keys)

        # Set up table keys
        for i in range(1, len(lines)):
            row = OrderedDict()
            state_transitions = lines[i]
            for j in range(len(keys)):
                row[keys[j]] = int(state_transitions[j])

            self.table.append(row)

    def build_state_token_list(self) -> None:
        """
        Constructs a list that can be accessed by state value to reference all tokens for final states. All state values
        are defined in the DFA created for this system

        :return: None
        """
        # Atomic lexical element states
        self.state_token[3] = constants.T_A_ID
        self.state_token[5] = constants.T_A_INTEGER
        self.state_token[17] = constants.T_A_FLOAT
        self.state_token[19] = constants.T_A_INTEGER

        # Reserved keyword/operator states
        self.state_token[22] = constants.T_R_EQUALS
        self.state_token[24] = constants.T_R_IS_EQUALS
        self.state_token[26] = constants.T_R_LESS_THAN
        self.state_token[28] = constants.T_R_LESS_THAN_OR_GREATER_THAN
        self.state_token[30] = constants.T_R_LESS_THAN_OR_EQUAL
        self.state_token[32] = constants.T_R_GREATER_THAN
        self.state_token[33] = constants.T_R_GREATER_THAN_OR_EQUAL
        self.state_token[34] = constants.T_R_SEMI_COLON
        self.state_token[35] = constants.T_R_COMMA
        self.state_token[36] = constants.T_R_DOT
        self.state_token[38] = constants.T_R_COLON
        self.state_token[39] = constants.T_R_DOUBLE_COLON
        self.state_token[40] = constants.T_R_PLUS
        self.state_token[41] = constants.T_R_MINUS
        self.state_token[42] = constants.T_R_MULTIPLY
        self.state_token[47] = constants.T_R_LINE_COMMENT
        self.state_token[60] = constants.T_R_LINE_COMMENT
        self.state_token[48] = constants.T_R_BLOCK_COMMENT
        self.state_token[59] = constants.T_R_DIVIDE
        self.state_token[50] = constants.T_R_OPEN_PARENTHESIS
        self.state_token[51] = constants.T_R_CLOSE_PARENTHESIS
        self.state_token[52] = constants.T_R_OPEN_BRACE
        self.state_token[53] = constants.T_R_CLOSE_BRACE
        self.state_token[54] = constants.T_R_OPEN_BRACKET
        self.state_token[55] = constants.T_R_CLOSE_BRACKET

        # Error states
        self.state_token[20] = constants.T_E_LEADING_ZERO
        self.state_token[58] = constants.T_E_LEADING_ZERO
        self.state_token[9] = constants.T_E_TRAILING_ZERO
        self.state_token[16] = constants.T_E_FLOAT_FORMAT
        self.state_token[49] = constants.T_E_BLOCK_COMMENT_FORMAT
        self.state_token[56] = constants.T_E_UNEXPECTED_CHAR

    def is_final_state(self, state: int) -> bool:
        """
        Check if the given state is a final state

        :param state: int, state to check
        :return: bool
        """
        return self.table[state]["Final_Token"] == 1

    def requires_back_track(self, state: int) -> bool:
        """
        Check if the given final state requires backtracking

        :param state: final state to check
        :return: bool
        """
        return self.table[state]["Back_Track"] == 1

    def get_state(self, current_state: int, current_char: str) -> int:
        """
        Get next state given the current state and an input character

        :param current_state:
        :param current_char:
        :return: int
        """
        return self.table[current_state][current_char]
