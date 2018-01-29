import unittest
from compiler.scanner.scanner import Token
from compiler.tools import constants


class TestToken(unittest.TestCase):
    def setUp(self):
        self.t = Token()

    def test_init(self):
        self.assertEqual(self.t.line, 0)
        self.assertEqual(self.t.column, 0)
        self.assertEqual(self.t.token, "")

    def test_is_error(self):
        self.t.token = constants.T_E_LEADING_ZERO
        self.assertEqual(self.t.is_error(), True)
        self.t.token = constants.T_E_TRAILING_ZERO
        self.assertEqual(self.t.is_error(), True)
        self.t.token = constants.T_E_FLOAT_FORMAT
        self.assertEqual(self.t.is_error(), True)
        self.t.token = constants.T_E_BLOCK_COMMENT_FORMAT
        self.assertEqual(self.t.is_error(), True)
        self.t.token = constants.T_E_UNEXPECTED_CHAR
        self.assertEqual(self.t.is_error(), True)


if __name__ == '__main__':
    unittest.main()
