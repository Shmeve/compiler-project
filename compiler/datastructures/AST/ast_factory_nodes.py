import abc


class Node(metaclass=abc.ABCMeta):
    def __init__(self, parent=None, leftmost_sibling=None, leftmost_child=None, right_sibling=None):
        self.parent = parent
        self.leftmost_sibling = leftmost_sibling
        self.leftmost_child = leftmost_child
        self.right_sibling = right_sibling

    def make_siblings(self, new_sibling):
        """
        Add node and all of its siblings to the current node's list of siblings

        :param new_sibling: sibling node to be added
        :return: None
        """
        current_ptr = self

        # Find right most sibling
        while current_ptr.right_sibling is not None:
            current_ptr = current_ptr.right_sibling

        # Join lists
        new_ptr = new_sibling.leftmost_sibling
        current_ptr.right_sibling = new_ptr

        # Set pointers for new siblings
        new_ptr.leftmost_sibling = self.leftmost_sibling
        new_ptr.parent = self.parent

        while new_ptr.right_sibling is not None:
            new_ptr = new_ptr.right_sibling
            new_ptr.leftmost_sibling = self.leftmost_sibling
            new_ptr.parent = self.parent

    def adopt_children(self, child_node):
        """
        Adopt a child and all of its siblings.

        :param child_node: child node to be adopted
        :return: None
        """
        # Make siblings of existing children
        if self.leftmost_child is not None:
            self.leftmost_child.make_siblings(child_node)
        # Start list of children
        else:
            child_ptr = child_node.leftmost_sibling
            self.leftmost_child = child_ptr

            while child_ptr is not None:
                child_ptr.parent = self
                child_ptr = child_ptr.right_sibling

    def make_family(self, parent, children: list):
        # TODO: This isn't supposed to be in Node
        """
        Iterate through list of children and adopt each one.

        :param parent: node adopting list of children
        :param children: list of child nodes to be adopted
        :return: None
        """
        for c in children:
            parent.adopt_children(c)


class ConcreteIntNumNode(Node):
    pass


class ConcreteIdNode(Node):
    pass


class ConcreteOpNode(Node):
    pass


class ConcreteNullNode(Node):
    pass
