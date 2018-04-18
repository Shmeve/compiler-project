import re
from compiler.semantic_analysis.visitor import Visitor
from compiler.datastructures.AST import ast_factory_nodes as fn


class ComputerMemSizeVisitor(Visitor):
    def propagate(self, p_node: fn.Node) -> None:
        if p_node.leftmost_child is not None:
            pointer: fn.Node = p_node.leftmost_child
            pointer.accept(self)

            while pointer.right_sibling is not None:
                pointer = pointer.right_sibling
                pointer.accept(self)

    def size_of_entry(self, p_node: fn.Node) -> int:
        size: int = 0
        dims = self.get_dims(p_node)
        raw_type = p_node.var_type.split('[', 1)[0]

        if raw_type == "int" or raw_type == "int:":
            size = 4
        elif raw_type == "float" or raw_type == "float:":
            size = 8
        # TODO: Uncomment for parsing
        # else:
        #     size = -p_node.symb_table.search(raw_type).element_link.table_size

        # Multiply by array dimensions
        for i in dims:
            size *= int(i)

        return size

    def size_of_type_node(self, p_node: fn.Node) -> int:
        """
        Determine size based on type

        :param p_node: node to determine size of
        :return: int
        """
        size: int = 0

        if p_node.var_type == "int":
            size = 4
        elif p_node.var_type == "float":
            size = 8

        return size

    def get_dims(self, p_node: fn.Node) -> list:
        """
        Helper function to parse a string to reconstruct list of array dimensions

        :param p_node: Node to process
        :return: list
        """
        dims = []
        var_type_copy = p_node.var_type  # Create copy of var type to modify

        # Check if var has dimensions
        if re.search('[\[[0-9]+\]]*$', var_type_copy):
            var_type_copy = var_type_copy.split('[', 1)[1]  # Cut leading var name before first dim
            dims_raw = var_type_copy.split(']')             # Split dimensions on remaining ']'
            dims_raw.pop()                                  # Remove empty last element caused by type ending in ']'

            # Remove leading [
            for i in dims_raw:
                if i[0] is '[':
                    i = i[1:]

                dims.append(i)

        return dims

    def visit_null_node_node(self, p_node: fn.ConcreteNullNode):
        self.propagate(p_node)

    def visit_prog_node(self, p_node: fn.ProgNode):
        self.propagate(p_node)

        p_node.symb_table.search("program").offset = p_node.symb_table.search("program").element_link.table_size

    def visit_class_list_node(self, p_node: fn.ClassListNode):
        self.propagate(p_node)

    def visit_func_def_list_node(self, p_node: fn.FuncDefListNode):
        self.propagate(p_node)

    def visit_stat_block_node(self, p_node: fn.StatBlockNode):
        self.propagate(p_node)

        if p_node.parent.node_type == "prog":
            for i in p_node.symb_table.symbols:
                i.offset = p_node.symb_table.table_size - i.size
                p_node.symb_table.table_size -= i.size

    def visit_class_decl_node(self, p_node: fn.ClassDeclNode):
        self.propagate(p_node)

        for i in p_node.symb_table.symbols:
            i.offset = p_node.symb_table.table_size - i.size
            p_node.symb_table.table_size -= i.size

        p_node.symb_table.parent_table.search(p_node.moon_var_name).offset = p_node.symb_table.table_size

    def visit_func_def_node(self, p_node: fn.FuncDefNode):
        self.propagate(p_node)

        p_node.symb_table.table_size = -(self.size_of_type_node(p_node.leftmost_child))
        p_node.symb_table.table_size -= 4

        for i in p_node.symb_table.symbols:
            i.offset = p_node.symb_table.table_size - i.size
            p_node.symb_table.table_size -= i.size

    def visit_id_node(self, p_node: fn.IdNode):
        self.propagate(p_node)

    def visit_type_node(self, p_node: fn.TypeNode):
        self.propagate(p_node)

    def visit_inher_list_node(self, p_node: fn.InherListNode):
        self.propagate(p_node)

    def visit_memb_list_node(self, p_node: fn.MembListNode):
        self.propagate(p_node)

    def visit_func_decl_node(self, p_node: fn.FuncDeclNode):
        self.propagate(p_node)

    def visit_f_param_node(self, p_node: fn.FparamNode):
        self.propagate(p_node)

        p_node.symb_table.search(p_node.moon_var_name).size = self.size_of_entry(p_node)

    def visit_var_decl_node(self, p_node: fn.VarDeclNode):
        self.propagate(p_node)

        p_node.symb_table.search(p_node.moon_var_name).size = self.size_of_entry(p_node)

    def visit_f_param_list_node(self, p_node: fn.FparamListNode):
        self.propagate(p_node)

    def visit_dim_list_node(self, p_node: fn.DimListNode):
        self.propagate(p_node)

    def visit_num_node(self, p_node: fn.NumNode):
        self.propagate(p_node)

        p_node.symb_table.search(p_node.moon_var_name).size = self.size_of_entry(p_node)

    def visit_if_stat_node(self, p_node: fn.IfStatNode):
        self.propagate(p_node)

    def visit_assign_stat_node(self, p_node: fn.AssignStatNode):
        self.propagate(p_node)

    def visit_for_stat_node(self, p_node: fn.ForStatNode):
        self.propagate(p_node)

    def visit_get_stat_node(self, p_node: fn.GetStatNode):
        self.propagate(p_node)

    def visit_put_stat_node(self, p_node: fn.PutStatNode):
        self.propagate(p_node)

    def visit_return_stat_node(self, p_node: fn.ReturnStatNode):
        self.propagate(p_node)

    def visit_add_op_node(self, p_node: fn.AddOpNode):
        self.propagate(p_node)

        p_node.symb_table.search(p_node.moon_var_name).size = self.size_of_entry(p_node)

    def visit_rel_expr_node(self, p_node: fn.RelExprNode):
        self.propagate(p_node)

    def visit_rel_op_node(self, p_node: fn.RelOpNode):
        self.propagate(p_node)

    def visit_mult_op_node(self, p_node: fn.MultOpNode):
        self.propagate(p_node)

        p_node.symb_table.search(p_node.moon_var_name).size = self.size_of_entry(p_node)

    def visit_not_node(self, p_node: fn.NotNode):
        self.propagate(p_node)

    def visit_sign_node(self, p_node: fn.SignNode):
        self.propagate(p_node)

    def visit_var_node(self, p_node: fn.VarNode):
        self.propagate(p_node)

        p_node.symb_table.search(p_node.moon_var_name).size = self.size_of_entry(p_node)

    def visit_data_member_node(self, p_node: fn.DataMemberNode):
        self.propagate(p_node)

    def visit_f_call_node(self, p_node: fn.FCallNode):
        self.propagate(p_node)

        p_node.symb_table.search(p_node.moon_var_name).size = self.size_of_entry(p_node)

    def visit_index_list_node(self, p_node: fn.IndexListNode):
        self.propagate(p_node)

    def visit_a_params_node(self, p_node: fn.AParamsNode):
        self.propagate(p_node)
