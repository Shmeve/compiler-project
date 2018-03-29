class LinkedListNode:
    def __init__(self, token="", next_node=None):
        self.token: str = token
        self.next_node: LinkedListNode = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head: LinkedListNode = head

    def insert_after(self, item: str, after_node: str=None) -> None:
        pointer: LinkedListNode = self.head
        insert_at_tail: bool = (after_node is None)

        if pointer is None:
            self.head = LinkedListNode(item)
            pointer = self.head
        else:
            if insert_at_tail:
                while pointer.next_node is not None:
                    pointer = pointer.next_node
            else:
                while pointer.token is not after_node:
                    pointer = pointer.next_node

            temp = pointer.next_node
            pointer.next_node = LinkedListNode(item, temp)

        return None

    def remove_node(self, item):
        pointer: LinkedListNode = self.head
        previous: LinkedListNode = None

        while pointer.token is not item:
            if pointer.next_node is None:
                return None

            previous = pointer
            pointer = pointer.next_node

        if previous is None:
            temp = self.head
            self.head = self.head.next_node
            temp.next_node = None
        else:
            previous.next_node = pointer.next_node

    def to_string(self) -> str:
        pointer: LinkedListNode = self.head
        string: str = pointer.token

        while pointer.next_node is not None:
            pointer = pointer.next_node
            string += " " + pointer.token

        return string

    def get_node(self, item) -> LinkedListNode:
        pointer: LinkedListNode = self.head

        while pointer.token is not item:
            pointer = pointer.next_node

        return pointer
