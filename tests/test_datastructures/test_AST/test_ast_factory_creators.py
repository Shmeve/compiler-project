import unittest
from compiler.datastructures.AST.ast_factory_nodes import Node
from compiler.datastructures.AST import ast_factory_creators


class TestAstFactoryCreators(unittest.TestCase):
    def test_make_node(self):
        int_node = ast_factory_creators.ConcreteIntNumCreator()
        id_node = ast_factory_creators.ConcreteIdCreator()
        op_node = ast_factory_creators.ConcreteOpCreator()

        self.assertEqual(True, True)

    def test_make_siblings(self):
        # create emtpy nodes
        node1: Node = ast_factory_creators.ConcreteNullCreator().node
        node2: Node = ast_factory_creators.ConcreteNullCreator().node
        node3: Node = ast_factory_creators.ConcreteNullCreator().node
        node4: Node = ast_factory_creators.ConcreteNullCreator().node

        node1.make_siblings(node2)  # add node 2 as sibling to node 1
        node3.make_siblings(node4)  # add node 4 as sibling to node 3
        node1.make_siblings(node4)  # add nodes 3 and 4 to 1 and 2

        ptr: Node = node1

        # Validate leftmost sibling order was respected
        #   i.e. Node1 -> Node2 -> Node3 -> Node4
        self.assertEqual(ptr.leftmost_sibling, ptr)
        self.assertEqual(ptr.right_sibling, node2)
        ptr = ptr.right_sibling
        self.assertEqual(ptr.right_sibling, node3)
        ptr = ptr.right_sibling
        self.assertEqual(ptr.right_sibling, node4)

    def test_adopt_children(self):
        # Create emtpy nodes
        node1: Node = ast_factory_creators.ConcreteNullCreator().node
        node2: Node = ast_factory_creators.ConcreteNullCreator().node
        node3: Node = ast_factory_creators.ConcreteNullCreator().node
        node4: Node = ast_factory_creators.ConcreteNullCreator().node

        # Create sibling relationship
        node2.make_siblings(node3)
        node2.make_siblings(node4)

        # Adopt a child
        node1.adopt_children(node2)

        # Validate child and all siblings adopted by parent
        self.assertEqual(node2.parent, node1)
        self.assertEqual(node3.parent, node1)
        self.assertEqual(node4.parent, node1)


if __name__ == '__main__':
    unittest.main()
