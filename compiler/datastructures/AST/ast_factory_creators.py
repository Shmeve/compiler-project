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


class ConcreteNullCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.ConcreteNullNode().build()


# New things
class ProgNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.ProgNode().build()


class ClassListNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.ClassListNode().build()


class FuncDefListNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.FuncDefListNode().build()


class StatBlockNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.StatBlockNode().build()


class ClassDeclNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.ClassDeclNode().build()


class FuncDefNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.FuncDefNode().build()


class IdNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.IdNode().build()


class TypeNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.TypeNode().build()


class InherListNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.InherListNode().build()


class MembListNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.MembListNode().build()


class FuncDeclNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.FuncDeclNode().build()


class FparamNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.FparamNode().build()


class VarDeclNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.VarDeclNode().build()


class FparamListNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.FparamListNode().build()


class DimListNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.DimListNode().build()


class NumNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.NumNode().build()


class IfStatNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.IfStatNode().build()


class AssignStatNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.AssignStatNode().build()


class ForStatNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.ForStatNode().build()


class GetStatNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.GetStatNode().build()


class PutStatNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.PutStatNode().build()


class ReturnStatNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.ReturnStatNode().build()


class AddOpNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.AddOpNode().build()


class RelExprNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.RelExprNode().build()


class RelOpNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.RelOpNode().build()


class MultOpNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.MultOpNode().build()


class NotNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.NotNode().build()


class SignNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.SignNode().build()


class VarNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.VarNode().build()


class DataMemberNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.DataMemberNode().build()


class FCallNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.FCallNode().build()


class IndexListNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.IndexListNode().build()


class AParamsNodeCreator(Creator):
    def _make_node(self) -> Node:
        return ast_factory_nodes.AParamsNode().build()

