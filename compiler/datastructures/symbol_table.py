class SymbolTableElement:
    def __init__(self, element_name: str="", element_kind: str="", element_type: str="", element_link=None):
        self.element_name = element_name
        self.element_kind = element_kind
        self.element_type = element_type
        self.element_link: SymbolTable = element_link


class SymbolTable:
    def __init__(self, table_name: str="", symbols: list=list(), table_size: int=0, table_level: int=0, parent_table=None):
        self.name = table_name
        self.symbols = symbols
        self.table_size = table_size
        self.table_level = table_level
        self.parent_table: SymbolTable = parent_table

    def insert(self, element: SymbolTableElement):
        """
        Add element to symbol table

        :param element: SymbolTableElement to add
        :return: SymbolTableElement
        """
        self.symbols.append(element)

    def search(self, search_element_name: str) -> SymbolTableElement:
        """
        Look for element in current table or preceding tables

        :param search_element_name: name of element being searched for
        :return: SymbolTableElement (Default null Element returned if not found)
        """
        found: bool = False

        for element in self.symbols:
            if element.element_name == search_element_name:
                found = True
                return element

        if not found and self.parent_table is not None:
            return self.parent_table.search(search_element_name)

        return SymbolTableElement()

    def delete(self):
        pass
