import abc
from compiler.datastructures.AST import ast_factory_nodes
from compiler.datastructures.AST.ast_factory_nodes import Node


class Creator(metaclass=abc.ABCMeta):
    def __init__(self):
        self.node = self._make_node()

    @abc.abstractmethod
    def _make_node(self):
        pass

    def make_siblings(self, new_sibling):
        self.node.make_siblings(new_sibling)

    def adopt_children(self, new_child):
        self.node.adopt_children(new_child)


class ConcreteIntNumCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.ConcreteIntNumNode()


class ConcreteIdCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.ConcreteIdNode()


class ConcreteOpCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.ConcreteOpNode()


class ConcreteNullCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.ConcreteNullNode()
