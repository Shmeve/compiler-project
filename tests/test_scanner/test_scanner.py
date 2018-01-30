import unittest
from compiler.scanner.scanner import Scanner
from compiler.tools import constants


class TestScanner(unittest.TestCase):
    def setUp(self):
        self.s: Scanner = Scanner("compiler/samples/sample_1")

        self.custom_input_path = 'tests/input/file'
        self.input = open(self.custom_input_path, 'w')

    def tearDown(self):
        self.input.close()

    def test_init(self):
        self.assertEqual(1, 1)

    def test_next_token(self):
        self.assertEqual(self.s.next_token().token, constants.T_R_INT)
        self.assertEqual(self.s.next_token().token, constants.T_A_ID)
        self.assertEqual(self.s.next_token().token, constants.T_R_FLOAT)
        self.assertEqual(self.s.next_token().token, constants.T_R_GET)
        self.assertEqual(self.s.next_token().token, constants.T_R_PUT)
        self.assertEqual(self.s.next_token().token, constants.T_A_INTEGER)
        self.assertEqual(self.s.next_token().token, constants.T_E_LEADING_ZERO)

    def test_T_E_ID(self):
        self.input.write("int in_t _int")
        self.input.close()

        s = Scanner(self.custom_input_path)
        s.scan_file()

        self.assertEqual(s.sequence[0].token, constants.T_R_INT)
        self.assertEqual(s.sequence[1].token, constants.T_A_ID)
        self.assertEqual(s.sequence[2].token, constants.T_E_UNEXPECTED_CHAR)
        self.assertEqual(s.sequence[3].token, constants.T_R_INT)

    def test_T_A__INTEGER(self):
        self.input.write("0123 123 123.")
        self.input.close()

        s = Scanner(self.custom_input_path)
        s.scan_file()

        self.assertEqual(s.sequence[0].token, constants.T_E_LEADING_ZERO)
        self.assertEqual(s.sequence[1].token, constants.T_A_INTEGER)
        self.assertEqual(s.sequence[2].token, constants.T_E_FLOAT_FORMAT)

    def test_T_A_FLOAT(self):
        self.input.write("01.23 12.340 012.340 12.34e1 12.34e+1 12.34e-0100 12.34")
        self.input.close()

        s = Scanner(self.custom_input_path)
        s.scan_file()

        # 01.23
        self.assertEqual(s.sequence[0].token, constants.T_E_LEADING_ZERO)
        self.assertEqual(s.sequence[1].token, constants.T_R_DOT)
        self.assertEqual(s.sequence[2].token, constants.T_A_INTEGER)
        # 12.340
        self.assertEqual(s.sequence[3].token, constants.T_E_TRAILING_ZERO)
        # 012.340
        self.assertEqual(s.sequence[4].token, constants.T_E_LEADING_ZERO)
        self.assertEqual(s.sequence[5].token, constants.T_R_DOT)
        self.assertEqual(s.sequence[6].token, constants.T_A_INTEGER)
        # 12.34e1
        self.assertEqual(s.sequence[7].token, constants.T_A_FLOAT)
        # 12.34e+1
        self.assertEqual(s.sequence[8].token, constants.T_A_FLOAT)
        # 12.34e-0100
        self.assertEqual(s.sequence[9].token, constants.T_E_LEADING_ZERO)
        # 12.34
        self.assertEqual(s.sequence[10].token, constants.T_A_FLOAT)

    def test_T_R_EQUALS_and_IS_EQUALS(self):
        self.input.write("= == === ====")
        self.input.close()

        s = Scanner(self.custom_input_path)
        s.scan_file()

        # =
        self.assertEqual(s.sequence[0].token, constants.T_R_EQUALS)
        # ==
        self.assertEqual(s.sequence[1].token, constants.T_R_IS_EQUALS)
        # ===
        self.assertEqual(s.sequence[2].token, constants.T_R_IS_EQUALS)
        self.assertEqual(s.sequence[3].token, constants.T_R_EQUALS)
        # ====
        self.assertEqual(s.sequence[4].token, constants.T_R_IS_EQUALS)
        self.assertEqual(s.sequence[5].token, constants.T_R_IS_EQUALS)

    def test_T_R_LESS_THAN_and_ambiguities(self):
        self.input.write("< <= <> <<>>")
        self.input.close()

        s = Scanner(self.custom_input_path)
        s.scan_file()

        # <
        self.assertEqual(s.sequence[0].token, constants.T_R_LESS_THAN)
        # <=
        self.assertEqual(s.sequence[1].token, constants.T_R_LESS_THAN_OR_EQUAL)
        # <>
        self.assertEqual(s.sequence[2].token, constants.T_R_LESS_THAN_OR_GREATER_THAN)
        # <<>>
        self.assertEqual(s.sequence[3].token, constants.T_R_LESS_THAN)
        self.assertEqual(s.sequence[4].token, constants.T_R_LESS_THAN_OR_GREATER_THAN)
        self.assertEqual(s.sequence[5].token, constants.T_R_GREATER_THAN)

    def test_T_R_DIVIDE_and_comment_ambiguities(self):
        self.input.write("/ //asd/asd\n/*abcd/*abcd/*abcd*/\n/*abcd123")
        self.input.close()

        s = Scanner(self.custom_input_path)
        s.scan_file()

        # /
        self.assertEqual(s.sequence[0].token, constants.T_R_DIVIDE)
        # //asd/asd\n
        self.assertEqual(s.sequence[1].token, constants.T_R_LINE_COMMENT)
        # /*abcd/*abcd/*abcd*/\n
        self.assertEqual(s.sequence[2].token, constants.T_R_BLOCK_COMMENT)
        # /*abcd123
        self.assertEqual(s.sequence[3].token, constants.T_E_BLOCK_COMMENT_FORMAT)

    def test_T_R_COLON_ambiguities(self):
        self.input.write(": :: ::: ::::")
        self.input.close()

        s = Scanner(self.custom_input_path)
        s.scan_file()

        # :
        self.assertEqual(s.sequence[0].token, constants.T_R_COLON)
        # ::
        self.assertEqual(s.sequence[1].token, constants.T_R_DOUBLE_COLON)
        # :::
        self.assertEqual(s.sequence[2].token, constants.T_R_DOUBLE_COLON)
        self.assertEqual(s.sequence[3].token, constants.T_R_COLON)
        # ::::
        self.assertEqual(s.sequence[4].token, constants.T_R_DOUBLE_COLON)
        self.assertEqual(s.sequence[5].token, constants.T_R_DOUBLE_COLON)

    def test_reserved_identifiers(self):
        self.input.write("and not or if then else for class int float\n"
                         "get put return program")
        self.input.close()

        s = Scanner(self.custom_input_path)
        s.scan_file()

        self.assertEqual(s.sequence[0].token, constants.T_R_AND)
        self.assertEqual(s.sequence[1].token, constants.T_R_NOT)
        self.assertEqual(s.sequence[2].token, constants.T_R_OR)
        self.assertEqual(s.sequence[3].token, constants.T_R_IF)
        self.assertEqual(s.sequence[4].token, constants.T_R_THEN)
        self.assertEqual(s.sequence[5].token, constants.T_R_ELSE)
        self.assertEqual(s.sequence[6].token, constants.T_R_FOR)
        self.assertEqual(s.sequence[7].token, constants.T_R_CLASS)
        self.assertEqual(s.sequence[8].token, constants.T_R_INT)
        self.assertEqual(s.sequence[9].token, constants.T_R_FLOAT)
        self.assertEqual(s.sequence[10].token, constants.T_R_GET)
        self.assertEqual(s.sequence[11].token, constants.T_R_PUT)
        self.assertEqual(s.sequence[12].token, constants.T_R_RETURN)
        self.assertEqual(s.sequence[13].token, constants.T_R_PROGRAM)

    def test_remaining_unambiguous_characters(self):
        self.input.write(",.+-*(){}[]")
        self.input.close()

        s = Scanner(self.custom_input_path)
        s.scan_file()

        self.assertEqual(s.sequence[0].token, constants.T_R_COMMA)
        self.assertEqual(s.sequence[1].token, constants.T_R_DOT)
        self.assertEqual(s.sequence[2].token, constants.T_R_PLUS)
        self.assertEqual(s.sequence[3].token, constants.T_R_MINUS)
        self.assertEqual(s.sequence[4].token, constants.T_R_MULTIPLY)
        self.assertEqual(s.sequence[5].token, constants.T_R_OPEN_PARENTHESIS)
        self.assertEqual(s.sequence[6].token, constants.T_R_CLOSE_PARENTHESIS)
        self.assertEqual(s.sequence[7].token, constants.T_R_OPEN_BRACE)
        self.assertEqual(s.sequence[8].token, constants.T_R_CLOSE_BRACE)
        self.assertEqual(s.sequence[9].token, constants.T_R_OPEN_BRACKET)
        self.assertEqual(s.sequence[10].token, constants.T_R_CLOSE_BRACKET)

    def test_T_R_GREATER_THAN_and_ambiguities(self):
        self.input.write("> >= >> ><")
        self.input.close()

        s = Scanner(self.custom_input_path)
        s.scan_file()

        # >
        self.assertEqual(s.sequence[0].token, constants.T_R_GREATER_THAN)
        # >=
        self.assertEqual(s.sequence[1].token, constants.T_R_GREATER_THAN_OR_EQUAL)
        # >>
        self.assertEqual(s.sequence[2].token, constants.T_R_GREATER_THAN)
        self.assertEqual(s.sequence[3].token, constants.T_R_GREATER_THAN)
        # ><
        self.assertEqual(s.sequence[4].token, constants.T_R_GREATER_THAN)
        self.assertEqual(s.sequence[5].token, constants.T_R_LESS_THAN)

    def test_next_char(self):
        self.assertEqual(self.s.next_char(), 'i')
        self.assertEqual(self.s.next_char(), 'n')
        self.assertEqual(self.s.next_char(), 't')
        self.assertEqual(self.s.next_char(), '\n')
        self.assertEqual(self.s.next_char(), 't')
        self.assertEqual(self.s.next_char(), 'e')
        self.assertEqual(self.s.next_char(), 's')
        self.assertEqual(self.s.next_char(), 't')

    def test_backup_char(self):
        # Skip to end of test file
        for i in range(8):
            self.s.next_char()

        self.assertEqual(self.s.current_char(), 't')
        self.assertEqual(self.s.backup_char(), 's')
        self.assertEqual(self.s.backup_char(), 'e')
        self.assertEqual(self.s.backup_char(), 't')
        self.assertEqual(self.s.backup_char(), '\n')
        self.assertEqual(self.s.backup_char(), 't')
        self.assertEqual(self.s.backup_char(), 'n')
        self.assertEqual(self.s.backup_char(), 'i')

    def test_lookup_token(self):
        self.assertEqual(self.s.lookup_token(3), constants.T_A_ID)
        self.assertEqual(self.s.lookup_token(5), constants.T_A_INTEGER)
        self.assertEqual(self.s.lookup_token(17), constants.T_A_FLOAT)
        self.assertEqual(self.s.lookup_token(1), "")    # Non final state look up


if __name__ == '__main__':
    unittest.main()
