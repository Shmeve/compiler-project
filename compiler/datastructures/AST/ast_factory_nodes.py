import abc
from compiler.scanner.token import Token


class Node(metaclass=abc.ABCMeta):
    def __init__(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, type=""):
        self.parent: Node = parent
        self.leftmost_sibling: Node = leftmost_sibling
        self.leftmost_child: Node = leftmost_child
        self.right_sibling: Node = right_sibling
        self.item: Token = item
        self.type: str = type

        if self.leftmost_sibling is None:
            self.leftmost_sibling = self

    def make_siblings(self, new_sibling):
        """
        Add node and all of its siblings to the current node's list of siblings

        :param new_sibling: sibling node to be added
        :return: None
        """
        current_ptr = self

        # Find right most sibling
        while current_ptr.right_sibling is not None:
            current_ptr = current_ptr.right_sibling

        # Join lists
        new_ptr = new_sibling.leftmost_sibling
        current_ptr.right_sibling = new_ptr

        # Set pointers for new siblings
        new_ptr.leftmost_sibling = self.leftmost_sibling
        new_ptr.parent = self.parent

        while new_ptr.right_sibling is not None:
            new_ptr = new_ptr.right_sibling
            new_ptr.leftmost_sibling = self.leftmost_sibling
            new_ptr.parent = self.parent

    def adopt_children(self, child_node):
        """
        Adopt a child and all of its siblings.

        :param child_node: child node to be adopted
        :return: None
        """
        # Make siblings of existing children
        if self.leftmost_child is not None:
            self.leftmost_child.make_siblings(child_node)
        # Start list of children
        else:
            child_ptr = child_node.leftmost_sibling
            self.leftmost_child = child_ptr

            while child_ptr is not None:
                child_ptr.parent = self
                child_ptr = child_ptr.right_sibling

    @abc.abstractmethod
    def build(self):
        pass


class ConcreteNullNode(Node):
    def build(self):
        self.type = "ConcreteNull"


# New things
class ProgNode(Node):
    def build(self):
        self.type = "prog"


class ClassListNode(Node):
    def build(self):
        self.type = "classList"


class FuncDefListNode(Node):
    def build(self):
        self.type = "funcDefList"


class StatBlockNode(Node):
    def build(self):
        self.type = "statBlock"


class ClassDeclNode(Node):
    def build(self):
        self.type = "classDecl"


class FuncDefNode(Node):
    def build(self):
        self.type = "funcDef"


class IdNode(Node):
    def build(self):
        self.type = "id"


class TypeNode(Node):
    def build(self):
        self.type = "type"


class InherListNode(Node):
    def build(self):
        self.type = "inherList"


class MembListNode(Node):
    def build(self):
        self.type = "membList"


class FuncDeclNode(Node):
    def build(self):
        self.type = "funcDecl"


class FparamNode(Node):
    def build(self):
        self.type = "fparam"


class VarDeclNode(Node):
    def build(self):
        self.type = "varDecl"


class FparamListNode(Node):
    def build(self):
        self.type = "fparamList"


class DimListNode(Node):
    def build(self):
        self.type = "dimList"


class NumNode(Node):
    def build(self):
        self.type = "num"


class IfStatNode(Node):
    def build(self):
        self.type = "ifStat"


class AssignStatNode(Node):
    def build(self):
        self.type = "assignStat"


class ForStatNode(Node):
    def build(self):
        self.type = "forStat"


class GetStatNode(Node):
    def build(self):
        self.type = "getStat"


class PutStatNode(Node):
    def build(self):
        self.type = "putStat"


class ReturnStatNode(Node):
    def build(self):
        self.type = "returnStat"


class AddOpNode(Node):
    def build(self):
        self.type = "addOp"


class RelExprNode(Node):
    def build(self):
        self.type = "relExpr"


class RelOpNode(Node):
    def build(self):
        self.type = "relOp"


class MultOpNode(Node):
    def build(self):
        self.type = "multOp"


class NotNode(Node):
    def build(self):
        self.type = "not"


class SignNode(Node):
    def build(self):
        self.type = "sign"


class VarNode(Node):
    def build(self):
        self.type = "var"


class DataMemberNode(Node):
    def build(self):
        self.type = "dataMember"


class FCallNode(Node):
    def build(self):
        self.type = "fCall"


class IndexListNode(Node):
    def build(self):
        self.type = "indexList"


class AParamsNode(Node):
    def build(self):
        self.type = "aParams"
