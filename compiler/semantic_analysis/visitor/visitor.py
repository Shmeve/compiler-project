import abc
from compiler.datastructures.AST import ast_factory_nodes as fn


class Visitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit_null_node_node(self, p_node: fn.ConcreteNullNode):
        pass

    @abc.abstractmethod
    def visit_prog_node(self, p_node: fn.ProgNode):
        pass

    @abc.abstractmethod
    def visit_class_list_node(self, p_node: fn.ClassListNode):
        pass

    @abc.abstractmethod
    def visit_func_def_list_node(self, p_node: fn.FuncDefListNode):
        pass

    @abc.abstractmethod
    def visit_stat_block_node(self, p_node: fn.StatBlockNode):
        pass

    @abc.abstractmethod
    def visit_class_decl_node(self, p_node: fn.ClassDeclNode):
        pass

    @abc.abstractmethod
    def visit_func_def_node(self, p_node: fn.FuncDefNode):
        pass

    @abc.abstractmethod
    def visit_id_node(self, p_node: fn.IdNode):
        pass

    @abc.abstractmethod
    def visit_type_node(self, p_node: fn.TypeNode):
        pass

    @abc.abstractmethod
    def visit_inher_list_node(self, p_node: fn.InherListNode):
        pass

    @abc.abstractmethod
    def visit_memb_list_node(self, p_node: fn.MembListNode):
        pass

    @abc.abstractmethod
    def visit_func_decl_node(self, p_node: fn.FuncDeclNode):
        pass

    @abc.abstractmethod
    def visit_f_param_node(self, p_node: fn.FparamNode):
        pass

    @abc.abstractmethod
    def visit_var_decl_node(self, p_node: fn.VarDeclNode):
        pass

    @abc.abstractmethod
    def visit_f_param_list_node(self, p_node: fn.FparamListNode):
        pass

    @abc.abstractmethod
    def visit_dim_list_node(self, p_node: fn.DimListNode):
        pass

    @abc.abstractmethod
    def visit_num_node(self, p_node: fn.NumNode):
        pass

    @abc.abstractmethod
    def visit_if_stat_node(self, p_node: fn.IfStatNode):
        pass

    @abc.abstractmethod
    def visit_assign_stat_node(self, p_node: fn.AssignStatNode):
        pass

    @abc.abstractmethod
    def visit_for_stat_node(self, p_node: fn.ForStatNode):
        pass

    @abc.abstractmethod
    def visit_get_stat_node(self, p_node: fn.GetStatNode):
        pass

    @abc.abstractmethod
    def visit_put_stat_node(self, p_node: fn.PutStatNode):
        pass

    @abc.abstractmethod
    def visit_return_stat_node(self, p_node: fn.ReturnStatNode):
        pass

    @abc.abstractmethod
    def visit_add_op_node(self, p_node: fn.AddOpNode):
        pass

    @abc.abstractmethod
    def visit_rel_expr_node(self, p_node: fn.RelExprNode):
        pass

    @abc.abstractmethod
    def visit_rel_op_node(self, p_node: fn.RelOpNode):
        pass

    @abc.abstractmethod
    def visit_mult_op_node(self, p_node: fn.MultOpNode):
        pass

    @abc.abstractmethod
    def visit_not_node(self, p_node: fn.NotNode):
        pass

    @abc.abstractmethod
    def visit_sign_node(self, p_node: fn.SignNode):
        pass

    @abc.abstractmethod
    def visit_var_node(self, p_node: fn.VarNode):
        pass

    @abc.abstractmethod
    def visit_data_member_node(self, p_node: fn.DataMemberNode):
        pass

    @abc.abstractmethod
    def visit_f_call_node(self, p_node: fn.FCallNode):
        pass

    @abc.abstractmethod
    def visit_index_list_node(self, p_node: fn.IndexListNode):
        pass

    @abc.abstractmethod
    def visit_a_params_node(self, p_node: fn.AParamsNode):
        pass
