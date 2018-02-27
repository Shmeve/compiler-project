import unittest
from compiler.parser.parser import ParsingTable


class TestParsingTable(unittest.TestCase):
    def test_build_table(self):
        self.p = ParsingTable()
        self.p.build_table()

        for k, v in self.p.parse_table.items():
            self.assertEqual(type(k), str)
            self.assertEqual(type(v), list)
            self.assertEqual(len(v), len(self.p.parse_table_inputs))

        self.assertEqual(True, True)

    def test_get_rule(self):
        self.parser = ParsingTable()
        self.parser.build_table()
        p = self.parser

        for input in p.parse_table_inputs:
            for value in p.parse_table.values():
                for v in value:
                    self.assertEqual(v <= 103, True)
                    self.assertEqual(type(v), int)


if __name__ == '__main__':
    unittest.main()
