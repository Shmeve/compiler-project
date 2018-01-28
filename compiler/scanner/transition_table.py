from collections import OrderedDict
import csv


class TransitionTable:
    def __init__(self, csv_path: str="compiler/tools/state_transition_table.csv"):
        """
        Constructor for TransitionTable object.

        :param csv_path: str, location of csv file to use when constructing the state transition table.
        """
        self.csv_path: str = csv_path
        self.table: list = []

    def build_table(self) -> None:
        """
        Create state transition table from CSV. The table is represented as a List of Dictionaries where the state
        to transition to can be accessed via table[currentState: int][inputKey: str].

        :return: None
        """
        with open(self.csv_path, newline='') as csvfile:
            lines = list(csv.reader(csvfile, delimiter=',', quotechar='"'))

        keys = lines[0]
        self.table.append(keys)

        # Set up table keys
        for i in range(1, len(lines)):
            row = OrderedDict()
            state_transitions = lines[i]
            for j in range(len(keys)):
                row[keys[j]] = state_transitions[j]

            self.table.append(row)
