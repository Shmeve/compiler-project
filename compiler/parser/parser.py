from compiler.datastructures.stack import Stack
from compiler.datastructures.linked_list import Node
from compiler.datastructures.linked_list import LinkedList
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
        self.sentential: LinkedList = LinkedList()

        self.token_sequence.append(Token(0, 0, '$'))

        # Set up parse table
        self.parse_table.build_table()

        self.output = []

    def parse(self) -> bool:
        """
        Parsing algorithm driver.

        :return: bool
        """
        end_token = Token(0, 0, '$')
        start_token = Token(0, 0, 'prog')

        # Initialize Sentential Form
        self.sentential.insert_after('prog')
        # Add initial Sentential Form to output
        d: dict = {
            "rule": "",
            "sentential": self.sentential.to_string()
        }
        self.output.append(d)

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

                if rule is not 105 and rule is not 106:
                    # Expand Sentential form
                    lhs = predict_set[str(rule)]["LHS"]
                    rhs = predict_set[str(rule)]["RHS"]

                    if len(rhs) is 1 and rhs[0] is "EPSILON":
                        # Remove LHS of production replace with nothing (EPSILON)
                        self.sentential.remove_node(lhs)
                    else:
                        sentential_index = self.sentential.get_node(lhs)        # Find LHS within the current Sentential
                        rhs_list = self.generate_linked_list_of_predict_rhs(rhs)  # Generate list of RHS to replace LHS

                        # Find end of new list to add within Sentential form LinkedList
                        tail: Node = rhs_list.head

                        while tail.next_node is not None:
                            tail = tail.next_node

                        # Insert new linked list after the LHS element of the predict set already in the Sentential
                        temp = sentential_index.next_node
                        sentential_index.next_node = rhs_list.head
                        tail.next_node = temp

                        # Remove LHS element from the list; Completing the replacement
                        self.sentential.remove_node(lhs)

                    # Log Rule Used and new Sentential Form
                    d: dict = {
                        "rule": rules[str(rule)],
                        "sentential": self.sentential.to_string()
                    }

                    self.stack.pop()
                    self.output.append(d)
                    self.inverse_rhs_multiple_push(rule)
                else:
                    # Check if an epsilon rule exists within grammar that might be missing from table
                    forced_epsilon_rule: str = self.check_for_epsilon_rule(x)

                    # No epsilon rule
                    if forced_epsilon_rule is "":
                        self.skip_errors()
                        self.error = True
                    # Epsilon rule exists, skip non-terminal
                    else:
                        if predict_set[forced_epsilon_rule]["RHS"][0] is "EPSILON":
                            self.stack.pop()
                            self.sentential.remove_node(predict_set[forced_epsilon_rule]["LHS"])

                            # Log Rule Used and new Sentential Form
                            d: dict = {
                                "rule": rules[forced_epsilon_rule],
                                "sentential": self.sentential.to_string()
                            }
                            self.output.append(d)
                        else:
                            rule = forced_epsilon_rule
                            # Expand Sentential form
                            lhs = predict_set[str(rule)]["LHS"]
                            rhs = predict_set[str(rule)]["RHS"]

                            if len(rhs) is 1 and rhs[0] is "EPSILON":
                                # Remove LHS of production replace with nothing (EPSILON)
                                self.sentential.remove_node(lhs)
                            else:
                                sentential_index = self.sentential.get_node(
                                    lhs)  # Find LHS within the current Sentential
                                rhs_list = self.generate_linked_list_of_predict_rhs(
                                    rhs)  # Generate list of RHS to replace LHS

                                # Find end of new list to add within Sentential form LinkedList
                                tail: Node = rhs_list.head

                                while tail.next_node is not None:
                                    tail = tail.next_node

                                # Insert new linked list after the LHS element of the predict set already in the Sentential
                                temp = sentential_index.next_node
                                sentential_index.next_node = rhs_list.head
                                tail.next_node = temp

                                # Remove LHS element from the list; Completing the replacement
                                self.sentential.remove_node(lhs)

                            # Log Rule Used and new Sentential Form
                            d: dict = {
                                "rule": rules[str(rule)],
                                "sentential": self.sentential.to_string()
                            }

                            self.stack.pop()
                            self.output.append(d)
                            self.inverse_rhs_multiple_push(rule)

        if t is not '$' or self.error:
            return False
        else:
            return True

    def skip_errors(self):
        # TODO: Implement error recovery
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

    def check_for_epsilon_rule(self, key: str) -> str:
        """
        Search all rules for key->EPSILON rule that was missing from generated grammar table

        :param key: non-terminal to search for epsilon production
        :return: str
        """
        for k, v in predict_set.items():
            if v["LHS"] is key and v["RHS"][0] is "EPSILON":
                return k

        # Check key->[Single Element Productions] since they may also lead to EPSILON
        for k, v in predict_set.items():
            if v["LHS"] is key:
                completed = True

                for i in v["RHS"]:
                    if self.check_for_epsilon_rule(i) is "":
                        completed = False
                        break
                if completed:
                    return k

        # TODO: the single production found is not being pushed to stack

        return ""

    def log_results(self, to_file: bool=False):
        """
        Log parser results, optionally file

        :param to_file: flag if logging should write to file
        :return: None
        """
        if to_file:
            file = 'output/parse'

            with open(file, 'w') as f:
                for l in self.output:
                    f.write("Rule Used: " + l["rule"] +"\n")
                    f.write("Sentential Form: " + l["sentential"] + "\n\n")
                    print("Rule Used: " + l["rule"])
                    print("Sentential Form: " + l["sentential"])
                    print("\n")
        else:
            for l in self.output:
                print("Rule Used: " + l["rule"])
                print("Sentential Form: " + l["sentential"])
                print("\n")

    def generate_linked_list_of_predict_rhs(self, rhs: list) -> LinkedList:
        """
        Create a linked list out of a predict set items RHS element

        :param rhs: list of items in the RHS
        :return: LinkedList
        """
        linked_list = LinkedList()

        for i in rhs:
            linked_list.insert_after(i)

        return linked_list
