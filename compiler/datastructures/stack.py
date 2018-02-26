from compiler.scanner.token import Token


class Stack:
    """
    Custom implementation of basic stack ADT using python list
    """

    def __init__(self):
        """
        Constructor, initialize empty list and size counter
        """
        self.stack: list = []
        self.size: int = 0

    def push(self, item: str) -> None:
        """
        Add item to top of stack
        :param item: item to add to stack
        :return: None
        """
        self.stack.append(item)
        self.size += 1

    def pop(self) -> str:
        """
        Remove and return item at top of stack.

        :return: str
        """
        if self.size > 0:
            item: str = self.stack.pop()
            self.size -= 1
        else:
            item = None

        return item

    def top(self) -> str:
        return self.stack[self.size-1]

    def size_of(self) -> int:
        """
        Get current amount of elements in stack.

        :return: int
        """
        return len(self.stack)

