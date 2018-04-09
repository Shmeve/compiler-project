import abc
from compiler.scanner.token import Token
from compiler.semantic_analysis.visitor.visitor import Visitor


class Node(metaclass=abc.ABCMeta):
    def __init__(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None, item=None, type=""):
        self.parent: Node = parent
        self.leftmost_sibling: Node = leftmost_sibling
        self.leftmost_child: Node = leftmost_child
        self.right_sibling: Node = right_sibling
        self.item: Token = item
        self.node_type: str = type

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

    @abc.abstractmethod
    def accept(self, p_visitor: Visitor):
        pass


class ConcreteNullNode(Node):
    def build(self):
        self.node_type = "ConcreteNull"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_null_node_node(self)


# New things
class ProgNode(Node):
    def build(self):
        self.node_type = "prog"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_prog_node(self)


class ClassListNode(Node):
    def build(self):
        self.node_type = "classList"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_class_list_node(self)


class FuncDefListNode(Node):
    def build(self):
        self.node_type = "funcDefList"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_func_def_list_node(self)


class StatBlockNode(Node):
    def build(self):
        self.node_type = "statBlock"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_stat_block_node(self)


class ClassDeclNode(Node):
    def build(self):
        self.node_type = "classDecl"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_class_decl_node(self)


class FuncDefNode(Node):
    def build(self):
        self.node_type = "funcDef"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_func_def_node(self)


class IdNode(Node):
    def build(self):
        self.node_type = "id"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_id_node(self)


class TypeNode(Node):
    def build(self):
        self.node_type = "type"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_type_node(self)


class InherListNode(Node):
    def build(self):
        self.node_type = "inherList"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_inher_list_node(self)


class MembListNode(Node):
    def build(self):
        self.node_type = "membList"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_memb_list_node(self)


class FuncDeclNode(Node):
    def build(self):
        self.node_type = "funcDecl"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_func_decl_node(self)


class FparamNode(Node):
    def build(self):
        self.node_type = "fparam"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_f_param_node(self)


class VarDeclNode(Node):
    def build(self):
        self.node_type = "varDecl"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_var_decl_node(self)


class FparamListNode(Node):
    def build(self):
        self.node_type = "fparamList"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_f_param_list_node(self)


class DimListNode(Node):
    def build(self):
        self.node_type = "dimList"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_dim_list_node(self)


class NumNode(Node):
    def build(self):
        self.node_type = "num"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_num_node(self)


class IfStatNode(Node):
    def build(self):
        self.node_type = "ifStat"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_if_stat_node(self)


class AssignStatNode(Node):
    def build(self):
        self.node_type = "assignStat"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_assign_stat_node(self)


class ForStatNode(Node):
    def build(self):
        self.node_type = "forStat"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_for_stat_node(self)


class GetStatNode(Node):
    def build(self):
        self.node_type = "getStat"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_get_stat_node(self)


class PutStatNode(Node):
    def build(self):
        self.node_type = "putStat"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_put_stat_node(self)


class ReturnStatNode(Node):
    def build(self):
        self.node_type = "returnStat"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_return_stat_node(self)


class AddOpNode(Node):
    def build(self):
        self.node_type = "addOp"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_add_op_node(self)


class RelExprNode(Node):
    def build(self):
        self.node_type = "relExpr"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_rel_expr_node(self)


class RelOpNode(Node):
    def build(self):
        self.node_type = "relOp"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_rel_op_node(self)


class MultOpNode(Node):
    def build(self):
        self.node_type = "multOp"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_mult_op_node(self)


class NotNode(Node):
    def build(self):
        self.node_type = "not"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_not_node(self)


class SignNode(Node):
    def build(self):
        self.node_type = "sign"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_sign_node(self)


class VarNode(Node):
    def build(self):
        self.node_type = "var"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_var_node(self)


class DataMemberNode(Node):
    def build(self):
        self.node_type = "dataMember"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_data_member_node(self)


class FCallNode(Node):
    def build(self):
        self.node_type = "fCall"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_f_call_node(self)


class IndexListNode(Node):
    def build(self):
        self.node_type = "indexList"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_index_list_node(self)


class AParamsNode(Node):
    def build(self):
        self.node_type = "aParams"

    def accept(self, p_visitor: Visitor) -> None:
        p_visitor.visit_a_params_node(self)
