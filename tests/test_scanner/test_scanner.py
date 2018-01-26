import unittest
from compiler.scanner.scanner import Scanner


class TestScanner(unittest.TestCase):
    def test_init(self):
        s: Scanner = Scanner("a.py")

        self.assertEqual(s.file, 'a.py')


if __name__ == '__main__':
    unittest.main()
