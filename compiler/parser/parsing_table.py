import json


class ParsingTable:
    def __init__(self, json_path: str="compiler/tools/parser/grammar_table.json"):
        """
        Constructor for the ParsingTable object.

        :param json_path:
        """
        self.parse_table_inputs: list = []
        self.parse_table: dict = {}

        with open(json_path) as json_data:
            self.json_data = json.load(json_data)
            json_data.close()

    def build_table(self) -> None:
        """
        Convert json output from http://hackingoff.com/compilers/ll-1-parser-generator into a usable table using python
        data structures.

        :return: None
        """
        self.parse_table_inputs = self.json_data.pop(0)     # Store header row
        self.parse_table_inputs.pop(0)                      # Pop leading buffer 0

        for row in self.json_data:
            key: str = row.pop(0)           # Pop string identifier (buffer)
            self.parse_table[key] = row     # Store remaining list under key

    def get_rule(self, current: str, parse_input: str) -> int:
        """
        Get rule of current row given a specific input

        :param current: string identifier of current row
        :param parse_input: string identifier of the input to search for rule
        :return: int (rule)
        """
        index: int = self.parse_table_inputs.index(parse_input)

        return self.parse_table[current][index]
