import unittest
from compiler.datastructures.AST.abstract_syntax_tree import AbstractSyntaxTree
from compiler.datastructures.AST.ast_factory_nodes import Node
from compiler.datastructures.AST import ast_factory_creators


class TestAbstractSyntaxTree(unittest.TestCase):
    def test_make_family(self):
        # Create AST
        ast = AbstractSyntaxTree()

        # Create emtpy nodes
        node1: Node = ast_factory_creators.ConcreteNullCreator().node   # Parent node
        node2: Node = ast_factory_creators.ConcreteNullCreator().node   # Child
        node3: Node = ast_factory_creators.ConcreteNullCreator().node   # Child
        node4: Node = ast_factory_creators.ConcreteNullCreator().node   # Child

        ast.make_family(node1, [node2, node3, node4])

        # Validate all children (2, 3, 4)  were made siblings under the parent node (1)
        self.assertEqual(node2.parent, node1)
        self.assertEqual(node3.parent, node1)
        self.assertEqual(node4.parent, node1)
        self.assertEqual(node2.right_sibling, node3)
        self.assertEqual(node3.right_sibling, node4)
        self.assertEqual(node4.right_sibling, None)


if __name__ == '__main__':
    unittest.main()
