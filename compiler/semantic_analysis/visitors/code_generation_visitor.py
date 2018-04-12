from compiler.semantic_analysis.visitor import Visitor
from compiler.datastructures.AST import ast_factory_nodes as fn


class CodeGenerationVisitor(Visitor):
    def __init__(self):
        self.available_registers: int = 12
        self.register_pool: list = []
        self.moon_exec_code: str = ""
        self.moon_data_code: str = ""
        self.moon_code_indent: str = "          "
        self.moon_output_file: str = "output/mooncode.m"

        for i in range(self.available_registers, 0, -1):
            self.register_pool.append('r'+str(i))

    def propagate(self, p_node: fn.Node) -> None:
        if p_node.leftmost_child is not None:
            pointer: fn.Node = p_node.leftmost_child
            pointer.accept(self)

            while pointer.right_sibling is not None:
                pointer = pointer.right_sibling
                pointer.accept(self)

    def visit_null_node_node(self, p_node: fn.ConcreteNullNode):
        # Propagate down
        self.propagate(p_node)

    def visit_prog_node(self, p_node: fn.ProgNode):
        # Propagate down
        self.propagate(p_node)

    def visit_class_list_node(self, p_node: fn.ClassListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_func_def_list_node(self, p_node: fn.FuncDefListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_stat_block_node(self, p_node: fn.StatBlockNode):
        # TODO: implement full (progStat in prog body)
        # Propagate down
        self.propagate(p_node)

    def visit_class_decl_node(self, p_node: fn.ClassDeclNode):
        # Propagate down
        self.propagate(p_node)

    def visit_func_def_node(self, p_node: fn.FuncDefNode):
        # TODO: implement full
        # Propagate down
        self.propagate(p_node)

    def visit_id_node(self, p_node: fn.IdNode):
        # Propagate down
        self.propagate(p_node)

    def visit_type_node(self, p_node: fn.TypeNode):
        # Propagate down
        self.propagate(p_node)

    def visit_inher_list_node(self, p_node: fn.InherListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_memb_list_node(self, p_node: fn.MembListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_func_decl_node(self, p_node: fn.FuncDeclNode):
        # Propagate down
        self.propagate(p_node)

    def visit_f_param_node(self, p_node: fn.FparamNode):
        # Propagate down
        self.propagate(p_node)

    def visit_var_decl_node(self, p_node: fn.VarDeclNode):
        # Propagate down
        self.propagate(p_node)

    def visit_f_param_list_node(self, p_node: fn.FparamListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_dim_list_node(self, p_node: fn.DimListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_num_node(self, p_node: fn.NumNode):
        # TODO: implement full
        # Propagate down
        self.propagate(p_node)

    def visit_if_stat_node(self, p_node: fn.IfStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_assign_stat_node(self, p_node: fn.AssignStatNode):
        # TODO: implement full
        # Propagate down
        self.propagate(p_node)

    def visit_for_stat_node(self, p_node: fn.ForStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_get_stat_node(self, p_node: fn.GetStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_put_stat_node(self, p_node: fn.PutStatNode):
        # TODO: implement full
        # Propagate down
        self.propagate(p_node)

    def visit_return_stat_node(self, p_node: fn.ReturnStatNode):
        # TODO: implement full
        # Propagate down
        self.propagate(p_node)

    def visit_add_op_node(self, p_node: fn.AddOpNode):
        # TODO: implement full
        # Propagate down
        self.propagate(p_node)

    def visit_rel_expr_node(self, p_node: fn.RelExprNode):
        # Propagate down
        self.propagate(p_node)

    def visit_rel_op_node(self, p_node: fn.RelOpNode):
        # Propagate down
        self.propagate(p_node)

    def visit_mult_op_node(self, p_node: fn.MultOpNode):
        # TODO: implement full
        # Propagate down
        self.propagate(p_node)

    def visit_not_node(self, p_node: fn.NotNode):
        # Propagate down
        self.propagate(p_node)

    def visit_sign_node(self, p_node: fn.SignNode):
        # Propagate down
        self.propagate(p_node)

    def visit_var_node(self, p_node: fn.VarNode):
        # Propagate down
        self.propagate(p_node)

    def visit_data_member_node(self, p_node: fn.DataMemberNode):
        # Propagate down
        self.propagate(p_node)

    def visit_f_call_node(self, p_node: fn.FCallNode):
        # TODO: implement full
        # Propagate down
        self.propagate(p_node)

    def visit_index_list_node(self, p_node: fn.IndexListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_a_params_node(self, p_node: fn.AParamsNode):
        # Propagate down
        self.propagate(p_node)