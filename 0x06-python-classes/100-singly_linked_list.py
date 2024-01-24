#!/usr/bin/python3
"""Defines a singly linked list"""


class Node:
    """Defines a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """Initializes a new node for a singly linked list

        Args:
            data (int): An integer data
            next_node (Node): A reference to the node following current node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data of the current node"""

        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data part of the current node

        Args:
                value (int): An integer data
        """

        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node part of the current node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Updates the next_node part of the current node

        Args:
            value (Node): An object/instance of class Node
        """

        # Set the next node ref if value is None or a type Node
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes a singly linked list"""

        self.head = None

    def prepend(self, new_node):
        """Adds a node at the beginnig of linked list"""

        new_node.next_node = self.head
        self.head = new_node

    def append(self, new_node):
        """Adds a node at the end of a linked list"""

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next_node:
            temp = temp.next_node
        temp.next_node = new_node

    def sorted_insert(self, value):
        """Inserts a node into a sorted singly linked list

        Args:
            value (int): An integer data
        """

        # Create a new_node
        new_node = Node(value)

        # If list is empty or new_node.data < firstnode.data
        if self.head is None or new_node.data < self.head.data:
            self.prepend(new_node)
            return

        temp = self.head
        while temp:
            if temp.next_node is None or temp.next_node.data > new_node.data:
                new_node.next_node = temp.next_node
                temp.next_node = new_node
                return
            temp = temp.next_node

    def __str__(self):
        """Returns ll elements when print is called on an instance"""

        current = self.head

        list_elems = []
        while current is not None:
            list_elems.append(str(current.data))
            current = current.next_node

        return "\n".join(list_elems)
