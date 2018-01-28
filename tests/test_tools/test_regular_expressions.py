import unittest
from compiler.tools import regular_expressions as RE


class TestScanner(unittest.TestCase):
    def test_l_e(self):
        self.assertEqual(RE.l_e("e"), False)
        self.assertEqual(RE.l_e("H"), True)

    def test_e(self):
        self.assertEqual(RE.e("e"), True)
        self.assertEqual(RE.e("1"), False)

    def test_d_0(self):
        self.assertEqual(RE.d_0("1"), True)
        self.assertEqual(RE.d_0("2"), True)
        self.assertEqual(RE.d_0("3"), True)
        self.assertEqual(RE.d_0("4"), True)
        self.assertEqual(RE.d_0("5"), True)
        self.assertEqual(RE.d_0("6"), True)
        self.assertEqual(RE.d_0("8"), True)
        self.assertEqual(RE.d_0("9"), True)
        self.assertEqual(RE.d_0("0"), False)

    def test_zero(self):
        self.assertEqual(RE.zero("0"), True)
        self.assertEqual(RE.zero("1"), False)


if __name__ == '__main__':
    unittest.main()
