#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Empty class Square."""

    def __init__(self, size=0):
        """Initialize the size of a new square

        Args:
            size (int): Size of a new square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns the area of the current square."""

        return self.__size * self.__size
