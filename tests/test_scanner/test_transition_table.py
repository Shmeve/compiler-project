import unittest
from compiler.scanner.transition_table import TransitionTable


class TestTransitionTable(unittest.TestCase):
    def setUp(self):
        self.table = TransitionTable("compiler/tools/state_transition_table.csv")
        self.table.build_table()
        self.table.build_state_token_list()

    def test_is_final_state(self):
        self.assertEqual(self.table.is_final_state(25), False)
        self.assertEqual(self.table.is_final_state(5), True)
        self.assertEqual(self.table.is_final_state(36), True)

    def test_get_state(self):
        self.assertEqual(self.table.get_state(1, 'non_e'), 2)
        self.assertEqual(self.table.get_state(1, 'e'), 2)
        self.assertEqual(self.table.get_state(3, 'non_zero'), 1)
        self.assertEqual(self.table.get_state(25, '+'), 26)


if __name__ == '__main__':
    unittest.main()
