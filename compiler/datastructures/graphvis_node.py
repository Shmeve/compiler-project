from compiler.datastructures.AST import ast_factory_nodes as fn


class GraphvizNode:
    def __init__(self, node: fn.Node, display_id: str):
        self.node = node
        self.display_id = display_id
