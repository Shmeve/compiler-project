import abc
from compiler.datastructures.AST import ast_factory_nodes
from compiler.datastructures.AST.ast_factory_nodes import Node


class Creator(metaclass=abc.ABCMeta):
    def __init__(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type=""):
        self.node = self._make_node(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)

    @abc.abstractmethod
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type=""):
        pass

    def make_siblings(self, new_sibling):
        self.node.make_siblings(new_sibling)

    def adopt_children(self, new_child):
        self.node.adopt_children(new_child)


class ConcreteNullCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.ConcreteNullNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


# New things
class ProgNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.ProgNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class ClassListNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.ClassListNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class FuncDefListNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.FuncDefListNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class StatBlockNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.StatBlockNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class ClassDeclNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.ClassDeclNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class FuncDefNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.FuncDefNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class IdNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.IdNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class TypeNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.TypeNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class InherListNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.InherListNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class MembListNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.MembListNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class FuncDeclNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.FuncDeclNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class FparamNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.FparamNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class VarDeclNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.VarDeclNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class FparamListNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.FparamListNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class DimListNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.DimListNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class NumNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.NumNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class IfStatNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.IfStatNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class AssignStatNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.AssignStatNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class ForStatNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.ForStatNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class GetStatNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.GetStatNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class PutStatNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.PutStatNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class ReturnStatNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.ReturnStatNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class AddOpNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.AddOpNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class RelExprNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.RelExprNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class RelOpNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.RelOpNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class MultOpNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.MultOpNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class NotNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.NotNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class SignNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.SignNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class VarNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.VarNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class DataMemberNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.DataMemberNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class FCallNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.FCallNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class IndexListNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.IndexListNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node


class AParamsNodeCreator(Creator):
    def _make_node(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, node_type="") -> Node:
        node = ast_factory_nodes.AParamsNode(parent, leftmost_sibling, leftmost_child, right_sibling, item, node_type)
        node.build()
        return node

