from compiler.datastructures.stack import Stack
from compiler.datastructures.linked_list import LinkedListNode
from compiler.datastructures.linked_list import LinkedList
from compiler.scanner.token import Token
from compiler.parser.parsing_table import ParsingTable
from compiler.tools.parser.grammar_components import terminals as terminals
from compiler.tools.parser.grammar_components import predict_set as predict_set
from compiler.tools.parser.grammar_components import rules as rules
from compiler.datastructures.AST import ast_factory_creators as fc
from compiler.datastructures.AST import ast_factory_nodes as fn
from compiler.datastructures.AST.abstract_syntax_tree import AbstractSyntaxTree
from compiler.datastructures.graphvis_node import GraphvizNode
from graphviz import Digraph


class Parser:
    def __init__(self, token_sequence: list):
        """
        Constructor to initialize parser.

        :param token_sequence: Sequence of Tokens produced by the Scanner to be parsed
        """
        self.ast = AbstractSyntaxTree()
        self.ast_root: fn.Node = None
        self.parse_stack: Stack = Stack()
        self.semantic_stack: list = []
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

        self.parse_stack.push(end_token.token)
        self.parse_stack.push(start_token.token)

        t: Token = self.next_token()

        while self.parse_stack.top() is not end_token.token:
            x = self.parse_stack.top()

            # Semantic action found
            if x[0] is "@":
                if x[1].isdigit():
                    # Build AST
                    ast_build_instructions: str = x[1:].split(',')
                    semantic_stack_pop_count = int(ast_build_instructions[0])
                    ast_parent_index = int(ast_build_instructions[1])-1
                    nodes = []

                    for i in range(0, semantic_stack_pop_count):
                        nodes.append(self.semantic_stack.pop())

                    nodes.reverse()
                    parent: fn.Node = nodes.pop(ast_parent_index)
                    subtree: fn.Node = self.ast.make_family(parent, nodes)
                    self.semantic_stack.append(subtree)
                    self.parse_stack.pop()
                else:
                    # Push to Semantic Stack
                    node_type: str = x[1:]                                    # Remove @ lead symbol for semantic action
                    create_node = self.node_of_type(node_type)                # Create the right node type

                    if self.save_token(node_type):
                        create_node.item = t                                  # Store token in node

                    self.semantic_stack.append(create_node)                   # Push node to semantic stack
                    self.parse_stack.pop()                                    # Parse next element
            # Current element is a terminal
            elif x in terminals:
                # Expected terminal
                if x is t.token:
                    self.parse_stack.pop()
                    t = self.next_token()
                # Unexpected terminal
                else:
                    self.skip_errors(t)
                    self.error = True
            # Skip EPSILONs
            elif x is "EPSILON":
                self.parse_stack.pop()
            # Current element is a non-terminal
            else:
                rule = self.parse_table.get_rule(x, t.token)

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
                        tail: LinkedListNode = rhs_list.head

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

                    self.parse_stack.pop()
                    self.output.append(d)
                    self.inverse_rhs_multiple_push(rule)
                else:
                    # Check if an epsilon rule exists within grammar that might be missing from table
                    forced_epsilon_rule: str = self.check_for_epsilon_rule(x)

                    # No epsilon rule
                    if forced_epsilon_rule is "":
                        self.skip_errors(t)
                        self.error = True
                    # Epsilon rule exists, skip non-terminal
                    else:
                        if predict_set[forced_epsilon_rule]["RHS"][0] is "EPSILON":
                            self.parse_stack.pop()
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
                                tail: LinkedListNode = rhs_list.head

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

                            self.parse_stack.pop()
                            self.output.append(d)
                            self.inverse_rhs_multiple_push(rule)

        self.ast_root = self.semantic_stack.pop()
        self.ast_touch_ups()
        self.visualize_ast('output/ast')

        if t.token is not '$' or self.error:
            return False
        else:
            return True

    def skip_errors(self, t: Token):
        # TODO: Implement error recovery
        self.parse_stack.pop()
        with open("output/parse_error", "a") as f:
            f.write(t.token + " " + str(t.line) + " " + str(t.column) + "\n")
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
            self.parse_stack.push(i)

    def check_for_epsilon_rule(self, key: str) -> str:
        """
        Search all rules for key->EPSILON rule that was missing from generated grammar table

        :param key: non-terminal to search for epsilon production
        :return: str
        """
        for k, v in predict_set.items():
            if v["LHS"] is key:
                if v["RHS"][0] is "EPSILON":
                    return k
                elif v["RHS"][0][0] is "@":
                    temp = v["RHS"]

                    while temp[0][0] is "@" and len(temp) > 1:
                        temp = temp[1:]

                    if temp[0] is "EPSILON":
                        return k

        # Check key->[Single Element Productions] since they may also lead to EPSILON
        for k, v in predict_set.items():
            if v["LHS"] is key:
                completed = True

                for i in v["RHS"]:
                    if self.check_for_epsilon_rule(i) is "" and i[0] is not "@":
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
            # Skip semantic actions (@prog, @4,1, etc)
            if i[0] is not "@":
                linked_list.insert_after(i)

        return linked_list

    def node_of_type(self, node_type: str) -> fn.Node:
        """
        Create a node based on the parsed semantic action (eg. @prog)

        :param node_type: type of node to create. (leading '@' stripped by parser
        :return: Node
        """
        if node_type == "prog":
            node = fc.ProgNodeCreator().node
            return node
        elif node_type == "classList":
            node = fc.ClassListNodeCreator().node
            return node
        elif node_type == "funcDefList":
            node = fc.FuncDefListNodeCreator().node
            return node
        elif node_type == "statBlock":
            node = fc.StatBlockNodeCreator().node
            return node
        elif node_type == "classDecl":
            node = fc.ClassDeclNodeCreator().node
            return node
        elif node_type == "funcDef":
            node = fc.FuncDefNodeCreator().node
            return node
        elif node_type == "id":
            node = fc.IdNodeCreator().node
            return node
        elif node_type == "type":
            node = fc.TypeNodeCreator().node
            return node
        elif node_type == "inherList":
            node = fc.InherListNodeCreator().node
            return node
        elif node_type == "membList":
            node = fc.MembListNodeCreator().node
            return node
        elif node_type == "funcDecl":
            node = fc.FuncDeclNodeCreator().node
            return node
        elif node_type == "fparam":
            node = fc.FparamNodeCreator().node
            return node
        elif node_type == "varDecl":
            node = fc.VarDeclNodeCreator().node
            return node
        elif node_type == "fparamList":
            node = fc.FparamListNodeCreator().node
            return node
        elif node_type == "dimList":
            node = fc.DimListNodeCreator().node
            return node
        elif node_type == "num":
            node = fc.NumNodeCreator().node
            return node
        elif node_type == "ifStat":
            node = fc.IfStatNodeCreator().node
            return node
        elif node_type == "assignStat":
            node = fc.AssignStatNodeCreator().node
            return node
        elif node_type == "forStat":
            node = fc.ForStatNodeCreator().node
            return node
        elif node_type == "getStat":
            node = fc.GetStatNodeCreator().node
            return node
        elif node_type == "putStat":
            node = fc.PutStatNodeCreator().node
            return node
        elif node_type == "returnStat":
            node = fc.ReturnStatNodeCreator().node
            return node
        elif node_type == "addOp":
            node = fc.AddOpNodeCreator().node
            return node
        elif node_type == "relExpr":
            node = fc.RelExprNodeCreator().node
            return node
        elif node_type == "relOp":
            node = fc.RelOpNodeCreator().node
            return node
        elif node_type == "multOp":
            node = fc.MultOpNodeCreator().node
            return node
        elif node_type == "not":
            node = fc.NotNodeCreator().node
            return node
        elif node_type == "sign":
            node = fc.SignNodeCreator().node
            return node
        elif node_type == "var":
            node = fc.VarNodeCreator().node
            return node
        elif node_type == "dataMember":
            node = fc.DataMemberNodeCreator().node
            return node
        elif node_type == "fCall":
            node = fc.FCallNodeCreator().node
            return node
        elif node_type == "indexList":
            node = fc.IndexListNodeCreator().node
            return node
        elif node_type == "aParams":
            node = fc.AParamsNodeCreator().node
            return node
        elif node_type == "null":
            node = fc.ConcreteNullCreator().node
            return node
        pass

    def visualize_ast(self, output_file: str) -> None:
        """
        Performs a Breadth First Search pass of the AST and produces a visualization of the graph using the Graphviz
        library

        :param root: Root of AST to visualize
        :param output_file: File path and name of where to store AST visualization
        :return: None
        """
        count: int = 0
        nodes_to_expand_remaining: bool = True
        pointer: fn.Node = self.ast_root
        search_queue: list = []

        # Initialize Graphviz with root node
        dot = Digraph()
        dot.node(str(count), pointer.node_type)

        # if pointer.item is not None:
        #     dot.node(str(count), pointer.node_type + "\n" + pointer.item.token + "\n" + pointer.item.lexeme)
        # else:
        #     dot.node(str(count), pointer.node_type)

        parent_id = str(count)

        while nodes_to_expand_remaining:
            pointer = pointer.leftmost_child
            count += 1
            search_queue.append(GraphvizNode(pointer, str(count)))

            if pointer.item is not None:
                dot.node(str(count), pointer.node_type + "\n" + pointer.item.token + "\n" + pointer.item.lexeme)
            else:
                dot.node(str(count), pointer.node_type)

            dot.edge(parent_id, str(count))

            # Link all siblings
            while pointer.right_sibling is not None:
                pointer = pointer.right_sibling
                count += 1
                search_queue.append(GraphvizNode(pointer, str(count)))

                if pointer.item is not None:
                    dot.node(str(count), pointer.node_type + "\n" + pointer.item.token + "\n" + pointer.item.lexeme)
                else:
                    dot.node(str(count), pointer.node_type)

                dot.edge(parent_id, str(count))

            while True:
                if len(search_queue) is 0:
                    nodes_to_expand_remaining = False
                    break

                next: GraphvizNode = search_queue.pop(0)

                if next.node.leftmost_child is not None:
                    parent_id = next.display_id
                    pointer = next.node
                    nodes_to_expand_remaining = True
                    break
                else:
                    nodes_to_expand_remaining = False

        dot.render(output_file, view=True)

    def save_token(self, node_type: str) -> bool:
        """
        Helper function used to determine if the node being created will require saving a token from
        self.token_sequence.

        :param node_type: type of node being created (leading '@' stripped by parser)
        :return: bool
        """
        # TODO: List all required node types
        nodes_requiring_token: list = [
            'prog',
            'type',
            'id',
            'num',
            'sign',
            'addOp',
            'multOp',
            'relOp'
        ]

        return node_type in nodes_requiring_token

    def ast_touch_ups(self) -> None:
        """
        Perform minor tweaks to fully generated AST to fix minor formatting issues.

        :return: None
        """
        nodes_to_expand_remaining: bool = True
        pointer: fn.Node = self.ast_root
        search_queue: list = []

        while nodes_to_expand_remaining:
            if pointer.leftmost_child is not None:
                pointer = pointer.leftmost_child

                # varDecl type id fix
                self.fix_vardecl_id_nodes(pointer)
                self.fix_lhs_var_in_assign_stat(pointer)

                search_queue.append(pointer)

                while pointer.right_sibling is not None:
                    pointer = pointer.right_sibling

                    # varDecl type id fix
                    self.fix_vardecl_id_nodes(pointer)
                    self.fix_lhs_var_in_assign_stat(pointer)

                    search_queue.append(pointer)

            if len(search_queue) > 0:
                pointer = search_queue[0]
                search_queue = search_queue[1:]
                nodes_to_expand_remaining = True
            else:
                nodes_to_expand_remaining = False

    def fix_vardecl_id_nodes(self, p: fn.Node) -> None:
        """
        Fix varDecl nodes where the type node was created as an id node

        :param p: Pointer to varDecl node in AST
        :return: None
        """
        if p.node_type == "varDecl":
            if p.leftmost_child.node_type == "id":
                temp: fn.Node = fc.TypeNodeCreator().node
                temp.item = p.leftmost_child.item
                temp.leftmost_sibling = temp
                temp.right_sibling = p.leftmost_child.right_sibling

                # Set all siblings leftmost sibling pointers
                t_point = temp
                while t_point.right_sibling is not None:
                    t_point = t_point.right_sibling
                    t_point.leftmost_sibling = temp

                p.leftmost_child.parent = None
                temp.parent = p
                p.leftmost_child = temp

    def fix_lhs_var_in_assign_stat(self, p: fn.Node) -> None:
        """
        Fix varElement order of var elements on LHS of assignStat elements

        :param p: pointer to assignStat node in AST
        :return: None
        """

        if p.node_type == "assignStat":
            if p.leftmost_child.leftmost_child.right_sibling is not None:
                head: fn.Node = p.leftmost_child.leftmost_child
                pointer: fn.Node = head
                temp: fn.Node

                while pointer.right_sibling is not None:
                    temp = pointer.right_sibling                # Node to shift to front
                    pointer.right_sibling = temp.right_sibling  # Step over node being moved
                    temp.right_sibling = head                   # Move node to front of list
                    head = temp                                 # Reassign head

                # Reset leftmost sibling values
                pointer = head
                head.leftmost_sibling = head

                while pointer.right_sibling is not None:
                    pointer = pointer.right_sibling
                    pointer.leftmost_sibling = head

                # Point parent (var) to new leftmost child
                head.parent.leftmost_child = head
