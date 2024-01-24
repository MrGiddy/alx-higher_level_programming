#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Empty class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the size of a new square

        Args:
            size (int): Size of a new square
        """
        self.__size = size
        self._position = position

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
                for x in range(self._position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """Retrieves the co-ordinates of the current square"""

        return self._position

    @position.setter
    def position(self, value):
        """Sets the co-ordinates of the current square"""

        if not all(isinstance(item, int) for item in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not all(i > 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self._position = value
