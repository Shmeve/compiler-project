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

    def test_requires_back_track(self):
        self.assertEqual(self.table.requires_back_track(3), True)
        self.assertEqual(self.table.requires_back_track(5), True)
        self.assertEqual(self.table.requires_back_track(9), True)
        self.assertEqual(self.table.requires_back_track(16), True)
        self.assertEqual(self.table.requires_back_track(17), True)
        self.assertEqual(self.table.requires_back_track(19), True)
        self.assertEqual(self.table.requires_back_track(20), True)
        self.assertEqual(self.table.requires_back_track(22), True)
        self.assertEqual(self.table.requires_back_track(24), True)
        self.assertEqual(self.table.requires_back_track(26), True)
        self.assertEqual(self.table.requires_back_track(28), True)
        self.assertEqual(self.table.requires_back_track(30), True)
        self.assertEqual(self.table.requires_back_track(32), True)
        self.assertEqual(self.table.requires_back_track(33), False)
        self.assertEqual(self.table.requires_back_track(34), False)
        self.assertEqual(self.table.requires_back_track(35), False)
        self.assertEqual(self.table.requires_back_track(36), False)
        self.assertEqual(self.table.requires_back_track(38), True)
        self.assertEqual(self.table.requires_back_track(39), False)

    def test_get_state(self):
        self.assertEqual(self.table.get_state(1, 'non_e'), 2)
        self.assertEqual(self.table.get_state(1, 'e'), 2)
        self.assertEqual(self.table.get_state(3, 'non_zero'), 1)
        self.assertEqual(self.table.get_state(25, '+'), 26)


if __name__ == '__main__':
    unittest.main()
