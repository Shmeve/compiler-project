class SymbolTable:
    def __init__(self, table_name: str="", symbols: list=list(), table_size: int=0, table_level: int=0, parent_table=None):
        self.name = table_name
        self.symbols = symbols
        self.table_size = table_size
        self.table_level = table_level
        self.parent_table = parent_table

    def insert(self):
        pass

    def search(self):
        pass

    def delete(self):
        pass


class SymbolTableElement:
    def __init__(self, element_name: str="", element_kind: str="", element_type: str="", element_link: SymbolTable=None):
        self.element_name = element_name
        self.element_kind = element_kind
        self.element_type = element_type
        self.element_link = element_link
