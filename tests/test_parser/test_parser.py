import unittest
from compiler.parser.parser import Parser
from compiler.scanner.scanner import Scanner
from compiler.tools import constants


class TestParser(unittest.TestCase):
    def setUp(self):
        with open('tests/input/file', 'w') as file:
            file.write("program{int x;};")
        self.s: Scanner = Scanner('tests/input/file')
        tokens: list = self.s.scan_file()

        self.p: Parser = Parser(tokens)

    def test_parse(self):
        self.assertEqual(self.p.parse(), True)

    def test_next_token(self):
        self.assertEqual(self.p.next_token().token, constants.T_R_PROGRAM)
        self.assertEqual(self.p.next_token().token, constants.T_R_OPEN_BRACE)
        self.assertEqual(self.p.next_token().token, constants.T_R_INT)
        self.assertEqual(self.p.next_token().token, constants.T_A_ID)
        self.assertEqual(self.p.next_token().token, constants.T_R_SEMI_COLON)
        self.assertEqual(self.p.next_token().token, constants.T_R_CLOSE_BRACE)
        self.assertEqual(self.p.next_token().token, constants.T_R_SEMI_COLON)

    def test_check_for_epsilon_rule(self):
        self.assertEqual(self.p.check_for_epsilon_rule("varOrFuncDeclHead") is not "", True)
        self.assertEqual(self.p.check_for_epsilon_rule("statBlock") is not "", True)
        self.assertEqual(self.p.check_for_epsilon_rule("idnestP") is not "", True)
        self.assertEqual(self.p.check_for_epsilon_rule("funcHead") is "", True)
        self.assertEqual(self.p.check_for_epsilon_rule("statement") is "", True)
        self.assertEqual(self.p.check_for_epsilon_rule("relExpr") is "", True)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
