import abc


class Visitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit_null_node_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_prog_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_class_list_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_func_def_list_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_stat_block_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_class_decl_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_func_def_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_id_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_type_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_inher_list_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_memb_list_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_func_decl_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_f_param_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_var_decl_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_f_param_list_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_dim_list_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_num_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_if_stat_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_assign_stat_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_for_stat_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_get_stat_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_put_stat_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_return_stat_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_add_op_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_rel_expr_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_rel_op_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_mult_op_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_not_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_sign_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_var_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_data_member_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_f_call_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_index_list_node(self, p_node):
        pass

    @abc.abstractmethod
    def visit_a_params_node(self, p_node):
        pass
