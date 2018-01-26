import unittest
from compiler.scanner.scanner import Token


class TestToken(unittest.TestCase):
    def test_init(self):
        t: Token = Token()

        self.assertEqual(t.line, 0)
        self.assertEqual(t.column, 0)
        self.assertEqual(t.lexeme, 0)


if __name__ == '__main__':
    unittest.main()
