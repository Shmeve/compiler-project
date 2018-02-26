from compiler.datastructures.stack import Stack
from compiler.scanner.token import Token
from compiler.parser.parsing_table import ParsingTable
from compiler.tools.parser.grammar_components import terminals as terminals
from compiler.tools.parser.grammar_components import predict_set as predict_set
from compiler.tools.parser.grammar_components import rules as rules


class Parser:
    def __init__(self, token_sequence: list):
        """
        Constructor to initialize parser.

        :param token_sequence: Sequence of Tokens produced by the Scanner to be parsed
        """
        self.stack: Stack = Stack()
        self.token_sequence: list = token_sequence
        self.parse_table: ParsingTable = ParsingTable()
        self.error: bool = False

        self.token_sequence.append(Token(0, 0, '$'))

        # Set up parse table
        self.parse_table.build_table()

    def parse(self) -> bool:
        """
        Parsing algorithm driver.

        :return: bool
        """
        end_token = Token(0, 0, '$')
        start_token = Token(0, 0, 'prog')

        self.stack.push(end_token.token)
        self.stack.push(start_token.token)

        t: str = self.next_token().token

        while self.stack.top() is not end_token.token:
            x = self.stack.top()

            # Current element is a terminal
            if x in terminals:
                # Expected terminal
                if x is t:
                    self.stack.pop()
                    t = self.next_token().token
                # Unexpected terminal
                else:
                    self.skip_errors()
                    self.error = True
            # Skip EPSILONs
            elif x is "EPSILON":
                self.stack.pop()
            # Current element is a non-terminal
            else:
                rule = self.parse_table.get_rule(x, t)

                if rule is not 102 and rule is not 103:
                    self.stack.pop()
                    print(rules[str(rule)])
                    self.inverse_rhs_multiple_push(rule)
                else:
                    self.skip_errors()
                    self.error = True

        if t is not '$' or self.error:
            return False
        else:
            return True

    def skip_errors(self):
        # TODO: Implement properly
        self.stack.pop()
        return None

    def next_token(self) -> Token:
        """
        Get next token in token sequence.

        :return: Token
        """
        return self.token_sequence.pop(0)

    def inverse_rhs_multiple_push(self, rule) -> None:
        """
        Expand non-terminal and place values into stack.

        :param rule: rule to expand into stack
        :return: None
        """
        rhs: list = predict_set[str(rule)]["RHS"]

        for i in reversed(rhs):
            self.stack.push(i)
