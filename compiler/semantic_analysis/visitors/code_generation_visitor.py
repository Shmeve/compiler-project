from compiler.semantic_analysis.visitor import Visitor
from compiler.datastructures.AST import ast_factory_nodes as fn
from compiler.datastructures.symbol_table import SymbolTable


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
        if p_node.parent.node_type == "prog":
            self.moon_exec_code += self.moon_code_indent + "entry\n"
            self.moon_exec_code += self.moon_code_indent + "addi r14,r0,topaddr\n"

            # Propagate down
            self.propagate(p_node)

            self.moon_data_code += self.moon_code_indent + "% buffer space used for console output\n"
            self.moon_data_code += self.moon_code_indent + "buf" + " res 20\n"
            # Halt
            self.moon_exec_code += self.moon_code_indent + "hlt\n"
        else:
            # Propagate down
            self.propagate(p_node)

    def visit_class_decl_node(self, p_node: fn.ClassDeclNode):
        # Propagate down
        self.propagate(p_node)

    def visit_func_def_node(self, p_node: fn.FuncDefNode):
        # TODO: func_def - Unconfirmed
        # Locate id node
        local_id_node: fn.Node

        if p_node.leftmost_child.right_sibling.right_sibling.node_type == "ConcreteNull":
            local_id_node = p_node.leftmost_child.right_sibling
        else:
            local_id_node = p_node.leftmost_child.right_sibling.right_sibling

        self.moon_exec_code += self.moon_code_indent + "% processing function definition: " + local_id_node.item.lexeme + "\n"
        self.moon_exec_code += self.moon_code_indent + local_id_node.item.lexeme + " sw -4(r14),r15\n"

        # Propagate down
        self.propagate(p_node)

        self.moon_exec_code += self.moon_code_indent + "lw r15, -4(r14)\n"
        self.moon_exec_code += self.moon_code_indent + "jr r15\n"

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
        # Propagate down
        self.propagate(p_node)

        # Allocate register
        local_register: str = self.register_pool.pop()

        # Generate Code
        self.moon_exec_code += self.moon_code_indent + "% processing: " + p_node.moon_var_name + ":=" + p_node.item.lexeme + "\n"
        self.moon_exec_code += self.moon_code_indent + "addi " + local_register + ",r0," + p_node.item.lexeme + "\n"
        self.moon_exec_code += self.moon_code_indent + "sw "+str(p_node.symb_table.search(p_node.moon_var_name).offset) + "(r14)," + local_register + "\n"

        # Free register
        self.register_pool.append(local_register)

    def visit_if_stat_node(self, p_node: fn.IfStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_assign_stat_node(self, p_node: fn.AssignStatNode):
        # Propagate down
        self.propagate(p_node)

        local_reg1: str = self.register_pool.pop()
        local_reg2: str = self.register_pool.pop()
        local_reg3: str = self.register_pool.pop()

        self.moon_exec_code += self.moon_code_indent + "% processing: " + p_node.leftmost_child.moon_var_name + " := " + p_node.leftmost_child.right_sibling.moon_var_name + "\n"
        self.moon_exec_code += self.moon_code_indent + "lw " + local_reg2 + "," + \
                               str(p_node.symb_table.search(p_node.leftmost_child.right_sibling.moon_var_name).offset) + "(r14)\n"
        self.moon_exec_code += self.moon_code_indent + "sw " + str(p_node.symb_table.search(p_node.leftmost_child.moon_var_name).offset) + "(r14)," + local_reg2 + "\n"

        self.register_pool.append(local_reg3)
        self.register_pool.append(local_reg2)
        self.register_pool.append(local_reg1)

    def visit_for_stat_node(self, p_node: fn.ForStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_get_stat_node(self, p_node: fn.GetStatNode):
        # Propagate down
        self.propagate(p_node)

    def visit_put_stat_node(self, p_node: fn.PutStatNode):
        # Propagate down
        self.propagate(p_node)

        # Get registers
        local_reg1: str = self.register_pool.pop()
        local_reg2: str = self.register_pool.pop()

        self.moon_exec_code += self.moon_code_indent + "% processing: put(" + p_node.leftmost_child.moon_var_name + ")\n"
        self.moon_exec_code += self.moon_code_indent + "lw " + local_reg1 + "," +\
                               str(p_node.symb_table.search(p_node.leftmost_child.moon_var_name).offset) + "(r14)\n"

        self.moon_exec_code += self.moon_code_indent + "sw -8(r14)," + local_reg1 + "\n"
        self.moon_exec_code += self.moon_code_indent + "% link buffer to stack\n"
        self.moon_exec_code += self.moon_code_indent + "addi " + local_reg1 + ",r0, buf\n"
        self.moon_exec_code += self.moon_code_indent + "sw -12(r14)," + local_reg1 + "\n"
        self.moon_exec_code += self.moon_code_indent + "% convert int to string for output\n"
        self.moon_exec_code += self.moon_code_indent + "jl r15, intstr\n"

        self.moon_exec_code += self.moon_code_indent + "sw -8(r14),r13\n"
        self.moon_exec_code += self.moon_code_indent + "% output to console\n"
        self.moon_exec_code += self.moon_code_indent + "jl r15, putstr\n"

        self.moon_exec_code += self.moon_code_indent + "subi r14,r14," + str(p_node.symb_table.table_size) + "\n"

        self.register_pool.append(local_reg2)
        self.register_pool.append(local_reg1)

    def visit_return_stat_node(self, p_node: fn.ReturnStatNode):
        # TODO: implement return_stat
        local_reg1 = self.register_pool.pop()

        # Propagate down
        self.propagate(p_node)

        self.moon_exec_code += self.moon_code_indent + "% processing: return(" + p_node.leftmost_child.moon_var_name + ")\n"
        self.moon_exec_code += self.moon_code_indent + "lw " + local_reg1 + "," + \
                               str(p_node.symb_table.search(p_node.leftmost_child.moon_var_name).offset) + "(r14)\n"
        self.moon_exec_code += self.moon_code_indent + "sw " + "0(r14)," + local_reg1 + "\n"

        self.register_pool.append(local_reg1)

    def visit_add_op_node(self, p_node: fn.AddOpNode):
        # Propagate down
        self.propagate(p_node)

        local_reg1: str = self.register_pool.pop()
        local_reg2: str = self.register_pool.pop()
        local_reg3: str = self.register_pool.pop()
        local_reg4: str = self.register_pool.pop()

        self.moon_exec_code += self.moon_code_indent + "% processing: " + p_node.moon_var_name + " := " + \
                              p_node.leftmost_child.moon_var_name + " + " + p_node.leftmost_child.right_sibling.moon_var_name + "\n"
        self.moon_exec_code += self.moon_code_indent + "lw " + local_reg2 + "," + str(p_node.symb_table.search(p_node.leftmost_child.moon_var_name).offset) + \
                              "(r14)\n"
        self.moon_exec_code += self.moon_code_indent + "lw " + local_reg3 + "," + str(p_node.symb_table.search(p_node.leftmost_child.right_sibling.moon_var_name).offset) + \
                              "(r14)\n"

        if p_node.item.token == "T_R_PLUS":
            self.moon_exec_code += self.moon_code_indent + "add " + local_reg4 + "," + local_reg2 + "," + local_reg3 + "\n"
        else:
            self.moon_exec_code += self.moon_code_indent + "sub " + local_reg4 + "," + local_reg2 + "," + local_reg3 + "\n"

        self.moon_exec_code += self.moon_code_indent + "sw " + str(p_node.symb_table.search(p_node.moon_var_name).offset) + "(r14)," + \
                               local_reg4 + "\n"

        self.register_pool.append(local_reg4)
        self.register_pool.append(local_reg3)
        self.register_pool.append(local_reg2)
        self.register_pool.append(local_reg1)

    def visit_rel_expr_node(self, p_node: fn.RelExprNode):
        # Propagate down
        self.propagate(p_node)

    def visit_rel_op_node(self, p_node: fn.RelOpNode):
        # Propagate down
        self.propagate(p_node)

    def visit_mult_op_node(self, p_node: fn.MultOpNode):
        # Propagate down
        self.propagate(p_node)

        local_reg1: str = self.register_pool.pop()
        local_reg2: str = self.register_pool.pop()
        local_reg3: str = self.register_pool.pop()
        local_reg4: str = self.register_pool.pop()

        # Generate Code
        self.moon_exec_code += self.moon_code_indent + '% processing: ' + p_node.moon_var_name + " := " + p_node.leftmost_child.moon_var_name + \
                               " * " + p_node.leftmost_child.right_sibling.moon_var_name + "\n"
        # Load to registers
        self.moon_exec_code += self.moon_code_indent + "lw " + local_reg2 + "," + \
                               str(p_node.symb_table.search(p_node.leftmost_child.moon_var_name).offset) + "(r14)\n"
        self.moon_exec_code += self.moon_code_indent + "lw " + local_reg3 + "," + \
                               str(p_node.symb_table.search(p_node.leftmost_child.right_sibling.moon_var_name).offset) + "(r14)\n"

        if p_node.item.token == "T_R_MULTIPLY":
            self.moon_exec_code += self.moon_code_indent + "mul " + local_reg4 + "," + local_reg2 + "," + local_reg3 + "\n"
        else:
            self.moon_exec_code += self.moon_code_indent + "div " + local_reg4 + "," + local_reg2 + "," + local_reg3 + "\n"

        self.moon_exec_code += self.moon_code_indent + "sw " + str(p_node.symb_table.search(p_node.moon_var_name).offset) + "(r14)," + local_reg4 + "\n"

        self.register_pool.append(local_reg4)
        self.register_pool.append(local_reg3)
        self.register_pool.append(local_reg2)
        self.register_pool.append(local_reg1)

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
        # TODO: f_call - Unconfirmed
        # Propagate down
        self.propagate(p_node)

        local_reg1 = self.register_pool.pop()
        params_list_node: fn.Node = p_node.leftmost_child.right_sibling
        param_pointer: fn.Node = params_list_node.leftmost_child
        function_table: SymbolTable = p_node.symb_table.search(p_node.leftmost_child.moon_var_name).element_link

        # Code generation
        self.moon_exec_code += self.moon_code_indent + "% processing: function call to " + p_node.leftmost_child.moon_var_name + "\n"

        # Loop on params:
        while param_pointer is not None:
            self.moon_exec_code += self.moon_code_indent + "lw " + local_reg1 + "," + \
                                   str(p_node.symb_table.search(param_pointer.moon_var_name).offset) + "(r14)\n"
            param_offset: int = p_node.symb_table.table_size + function_table.search(param_pointer.moon_var_name).offset
            # param_offset: int = p_node.symb_table.table_size + p_node.symb_table.search(param_pointer.moon_var_name).offset
            self.moon_exec_code += self.moon_code_indent + "sw " + str(param_offset) + "(r14)," + local_reg1 + "\n"

            param_pointer = param_pointer.right_sibling

        self.moon_exec_code += self.moon_code_indent + "addi r14,r14," + str(p_node.symb_table.table_size) + "\n"
        self.moon_exec_code += self.moon_code_indent + "jl r15," + p_node.leftmost_child.moon_var_name + "\n"  # TODO: generate random name
        self.moon_exec_code += self.moon_code_indent + "subi r14,r14," + str(p_node.symb_table.table_size) + "\n"

        self.moon_exec_code += self.moon_code_indent + "lw " + local_reg1 + "," + str(p_node.symb_table.table_size) + "(r14)\n"
        self.moon_exec_code += self.moon_code_indent + "sw " + str(p_node.symb_table.search(p_node.moon_var_name).offset) + \
                               "(r14)," + local_reg1 + "\n"

        self.register_pool.append(local_reg1)

    def visit_index_list_node(self, p_node: fn.IndexListNode):
        # Propagate down
        self.propagate(p_node)

    def visit_a_params_node(self, p_node: fn.AParamsNode):
        # Propagate down
        self.propagate(p_node)