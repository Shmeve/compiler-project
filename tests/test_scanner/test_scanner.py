import unittest
from compiler.scanner.scanner import Scanner
from compiler.tools import constants


class TestScanner(unittest.TestCase):
    def setUp(self):
        self.s: Scanner = Scanner("compiler/samples/sample_1")

    def test_init(self):
        self.assertEqual(1, 1)

    def test_next_token(self):
        self.assertEqual(self.s.next_token().lexeme, constants.T_R_INT)
        self.assertEqual(self.s.next_token().lexeme, constants.T_A_ID)
        self.assertEqual(self.s.next_token().lexeme, constants.T_R_FLOAT)
        self.assertEqual(self.s.next_token().lexeme, constants.T_R_GET)
        self.assertEqual(self.s.next_token().lexeme, constants.T_R_PUT)
        self.assertEqual(self.s.next_token().lexeme, constants.T_A_INTEGER)
        self.assertEqual(self.s.next_token().lexeme, constants.T_E_LEADING_ZERO)

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
