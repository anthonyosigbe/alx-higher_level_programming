#!/usr/bin/python3
"""Create classes for a singly-linked list."""


class Node:
    """Describe a node within a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Create a new Node instance.

        Args:
            data (int): The data for the new Node.
            next_node (Node): The subsequent node for the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve or update the data within the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve or modify the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Describe a singly-linked list."""
    def __init__(self):
        """Create a new instance of SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Add a new Node to the SinglyLinkedList,
        in its proper numerical order.

        Args:
            value (Node): The Node to be inserted.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Specify the print() representation for a SinglyLinkedList."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
