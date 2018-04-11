from compiler.datastructures.AST import ast_factory_nodes as fn
from compiler.semantic_analysis.visitors.symbol_table_creation_visitor import SymbolTableCreationVisitor
from compiler.datastructures.symbol_table import SymbolTable
from terminaltables import AsciiTable


class SemanticAnalyzer:
    def __init__(self, ast_root_node: fn.Node):
        self.ast_root_node = ast_root_node
        self.global_table = None

    def analyze(self):
        table_creation_visitor = SymbolTableCreationVisitor()

        self.ast_root_node.accept(table_creation_visitor)
        self.global_table = self.ast_root_node.symb_table

    def output_tables(self, root_table: SymbolTable):
        # TODO: Return string and write to file
        title: str = root_table.name
        data = [
            ['Name', 'Kind', 'Type', 'Link']
        ]

        # Set up table data
        for s in root_table.symbols:
            row = [
                s.element_name,
                s.element_kind,
                s.element_type
            ]

            if s.element_link is not None:
                row.append("\u2714")
            else:
                row.append("\u2A2F")

            data.append(row)

        # Draw table
        padding: str = ""

        for i in range(0, root_table.table_level):
            padding += '\t'

        table = AsciiTable(data, title)
        output = table.table.replace('\n', '\n'+padding)
        print(padding+output)

        # Draw children
        for s in root_table.symbols:
            if s.element_link is not None:
                self.output_tables(s.element_link)
