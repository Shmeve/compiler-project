from compiler.datastructures.AST.ast_factory_nodes import Node


class AbstractSyntaxTree:
    def __init__(self):
        pass

    def make_family(self, parent: Node, children: list) -> Node:
        """
        Iterate through list of children and adopt each one.

        :param parent: node adopting list of children
        :param children: list of child nodes to be adopted
        :return: Node
        """
        for c in children:
            parent.adopt_children(c)

        return parent
