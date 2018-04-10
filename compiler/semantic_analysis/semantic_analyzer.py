from compiler.datastructures.AST import ast_factory_nodes as fn
from compiler.semantic_analysis.visitors.symbol_table_creation_visitor import SymbolTableCreationVisitor
from compiler.datastructures.symbol_table import SymbolTable


class SemanticAnalyzer:
    def __init__(self, ast_root_node: fn.Node):
        self.ast_root_node = ast_root_node
        self.global_table = SymbolTable("Global")

    def analyze(self):
        table_creation_visitor = SymbolTableCreationVisitor()

        self.ast_root_node.accept(table_creation_visitor)
