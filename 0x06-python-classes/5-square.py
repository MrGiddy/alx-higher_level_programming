#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Empty class Square."""

    def __init__(self, size=0):
        """Initialize the size of a new square

        Args:
            size (int): Size of a new square
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the current square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the current square"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the area of the current square."""

        return self.__size * self.__size

    def my_print(self):
        """Prints the current square using #'s"""

        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
