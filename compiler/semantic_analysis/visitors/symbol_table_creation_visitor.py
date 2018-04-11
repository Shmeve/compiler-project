from compiler.semantic_analysis.visitor import Visitor
from compiler.datastructures.AST import ast_factory_nodes as fn
from compiler.datastructures.symbol_table import SymbolTable, SymbolTableElement


class SymbolTableCreationVisitor(Visitor):
    def __init__(self):
        self.temp_var_num = 0

    def get_temp_var_name(self) -> str:
        self.temp_var_num += 1
        return "t" + str(self.temp_var_num)

    def propagate(self, p_node: fn.Node):
        # Propagate down
        if p_node.leftmost_child is not None:
            pointer: fn.Node = p_node.leftmost_child
            pointer.symb_table = p_node.symb_table
            pointer.accept(self)

            while pointer.right_sibling is not None:
                pointer = pointer.right_sibling
                pointer.symb_table = p_node.symb_table
                pointer.accept(self)

    def visit_null_node_node(self, p_node: fn.ConcreteNullNode):
        pass

    def visit_prog_node(self, p_node: fn.ProgNode):
        p_node.symb_table = SymbolTable("Global")

        self.propagate(p_node)

    def visit_class_list_node(self, p_node: fn.ClassListNode):
        self.propagate(p_node)

    def visit_func_def_list_node(self, p_node: fn.FuncDefListNode):
        self.propagate(p_node)

    def visit_stat_block_node(self, p_node: fn.StatBlockNode):
        if p_node.parent.node_type == "prog":
            local_table: SymbolTable = SymbolTable(table_name="Program", symbols=[],
                                                   table_level=1, parent_table=p_node.symb_table)
            local_entry: SymbolTableElement = SymbolTableElement("program", "function", "", local_table)
            p_node.symb_table.insert(local_entry)
            p_node.symb_table = local_table

        self.propagate(p_node)

    def visit_class_decl_node(self, p_node: fn.ClassDeclNode):
        class_name: str = p_node.leftmost_child.item.lexeme
        local_table: SymbolTable = SymbolTable(table_name=class_name,
                                               symbols=[],
                                               table_level=p_node.symb_table.table_level + 1,
                                               table_size=0,
                                               parent_table=p_node.symb_table)
        local_entry: SymbolTableElement = SymbolTableElement(class_name, "class", "", local_table)
        p_node.symb_table.insert(local_entry)
        p_node.symb_table = local_table

        self.propagate(p_node)

    def visit_func_def_node(self, p_node: fn.FuncDefNode):
        function_type: str = p_node.leftmost_child.item.lexeme
        function_name: str
        function_scope: str
        function_name_full: str
        function_param_types: str = ""
        class_function: bool = False

        if p_node.leftmost_child.right_sibling.right_sibling.node_type == "ConcreteNull":
            # Null Scope
            function_name = p_node.leftmost_child.right_sibling.item.lexeme
            function_name_full = function_name
        else:
            # Scoped function
            function_scope = p_node.leftmost_child.right_sibling.item.lexeme
            function_name = p_node.leftmost_child.right_sibling.right_sibling.item.lexeme
            function_name_full = function_scope + "::" + function_name
            class_function = True

        param_list: fn.Node = p_node.leftmost_child.right_sibling.right_sibling.right_sibling
        function_params: list = list()

        # Get parameter nodes
        if param_list.leftmost_child is not None:
            pointer: fn.Node = param_list.leftmost_child
            function_params.append(pointer)

            while pointer.right_sibling is not None:
                pointer = pointer.right_sibling
                function_params.append(pointer)

        # Create string for node types
        for node in function_params:
            dimList: fn.Node = node.leftmost_child.right_sibling.right_sibling
            function_param_types += node.leftmost_child.item.lexeme

            if dimList.leftmost_child is not None:
                p: fn.Node = dimList.leftmost_child
                function_param_types += '['+p.item.lexeme+']'

                while p.right_sibling is not None:
                    p = p.right_sibling
                    function_param_types += '['+p.item.lexeme+']'

            function_param_types += ','

        # Remove trailing commas
        if len(function_param_types) > 0 and function_param_types[len(function_param_types)-1] == ',':
            function_param_types = function_param_types[:-1]

        # Create new entry and table
        local_table: SymbolTable = SymbolTable(table_name=function_name_full, symbols=[])
        local_entry: SymbolTableElement = SymbolTableElement(function_name, "function",
                                                             function_type+': '+function_param_types,
                                                             local_table)
        if class_function:
            inserting_table: SymbolTable = p_node.symb_table.search(function_scope).element_link
            inserting_element: SymbolTableElement = inserting_table.search(function_name)
            inserting_element.element_link = local_table
            local_table.parent_table = inserting_table
            local_table.table_level = inserting_table.table_level+1
        else:
            p_node.symb_table.insert(local_entry)
            local_table.parent_table = p_node.symb_table
            local_table.table_level = p_node.symb_table.table_level + 1

        p_node.symb_table = local_table

        # Propagate down
        self.propagate(p_node)

    def visit_id_node(self, p_node: fn.IdNode):
        pass

    def visit_type_node(self, p_node: fn.TypeNode):
        pass

    def visit_inher_list_node(self, p_node: fn.InherListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_memb_list_node(self, p_node: fn.MembListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_func_decl_node(self, p_node: fn.FuncDeclNode):
        func_type: str = p_node.leftmost_child.item.lexeme
        func_id: str = p_node.leftmost_child.right_sibling.item.lexeme
        func_params: list = []

        # Collect Params
        fparam_list = p_node.leftmost_child.right_sibling.right_sibling

        # Check for Params
        if fparam_list.leftmost_child is not None:
            pointer: fn.Node = fparam_list.leftmost_child
            dims = pointer.leftmost_child.right_sibling.right_sibling
            param: str = pointer.leftmost_child.item.lexeme

            # Process dimList
            if dims.leftmost_child is not None:
                dim = dims.leftmost_child
                param += '[' + dim.item.lexeme + ']'

                while dim.right_sibling is not None:
                    dim = dim.right_sibling
                    param += '[' + dim.item.lexeme + ']'

            func_params.append(param)

            # Process remaining Params
            while pointer.right_sibling is not None:
                pointer = pointer.right_sibling
                dims = pointer.leftmost_child.right_sibling.right_sibling
                param: str = pointer.leftmost_child.item.lexeme

                # Process dimList
                if dims.leftmost_child is not None:
                    dim = dims.leftmost_child
                    param += '[' + dim.item.lexeme + ']'

                    while dim.right_sibling is not None:
                        dim = dim.right_sibling
                        param += '[' + dim.item.lexeme + ']'

                func_params.append(param)

        # Format type string
        if len(func_params) > 0:
            func_type += ': '
            for p in func_params:
                func_type += p + ','

        # Create entry
        local_entry: SymbolTableElement = SymbolTableElement(func_id, "function", func_type)
        p_node.symb_table.insert(local_entry)

        # Propagate down
        self.propagate(p_node)

    def visit_f_param_node(self, p_node: fn.FparamNode):
        # Propagate down
        self.propagate(p_node)

    def visit_var_decl_node(self, p_node: fn.VarDeclNode):
        # Propagate downwards first
        self.propagate(p_node)

        # Process node
        var_type: str = p_node.leftmost_child.item.lexeme
        var_id: str = p_node.leftmost_child.right_sibling.item.lexeme
        var_dims = list()

        # Collect dim numbers
        dim_list: fn.Node = p_node.leftmost_child.right_sibling.right_sibling
        if dim_list.leftmost_child is not None:
            p = dim_list.leftmost_child
            var_dims.append(p.item.lexeme)

            while p.right_sibling is not None:
                p = p.right_sibling
                var_dims.append(p.item.lexeme)

        # Append dims to type
        for d in var_dims:
            var_type += '[' + d + ']'

        # Create entry
        local_entry: SymbolTableElement = SymbolTableElement(var_id, "variable", var_type)
        p_node.symb_table.insert(local_entry)

    def visit_f_param_list_node(self, p_node: fn.FparamListNode):
        pass

    def visit_dim_list_node(self, p_node: fn.DimListNode):
        pass

    def visit_num_node(self, p_node: fn.NumNode):
        pass

    def visit_if_stat_node(self, p_node: fn.IfStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_assign_stat_node(self, p_node: fn.AssignStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_for_stat_node(self, p_node: fn.ForStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_get_stat_node(self, p_node: fn.GetStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_put_stat_node(self, p_node: fn.PutStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_return_stat_node(self, p_node: fn.ReturnStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_add_op_node(self, p_node: fn.AddOpNode):
        # Propagate down
        self.propagate(p_node)

        # Temp var
        temp_var_name = self.get_temp_var_name()
        p_node.moon_var_name = temp_var_name

        # Setup entry
        local_entry: SymbolTableElement = SymbolTableElement(temp_var_name, "Temp Var", p_node.var_type)
        p_node.symb_table.insert(local_entry)

    def visit_rel_expr_node(self, p_node: fn.RelExprNode):
        # Propagate down
        self.propagate(p_node)

    def visit_rel_op_node(self, p_node: fn.RelOpNode):
        pass

    def visit_mult_op_node(self, p_node: fn.MultOpNode):
        # Propagate down
        self.propagate(p_node)

        # Temp var
        temp_var_name = self.get_temp_var_name()
        p_node.moon_var_name = temp_var_name

        # Dims

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
        # Propagate down
        self.propagate(p_node)

    def visit_index_list_node(self, p_node: fn.IndexListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_a_params_node(self, p_node: fn.AParamsNode):
        # Propagate down
        self.propagate(p_node)
