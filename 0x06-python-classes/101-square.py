#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Empty class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the size of a new square

        Args:
            size (int): Size of a new square
        """
        self.size = size
        self.position = position

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

        elems = []
        if (self.__size == 0):
            print()
            elems.append("\n")
        else:
            for y in range(self._position[1]):
                print("")
                elems.append("\n")
            for i in range(self.__size):
                for x in range(self._position[0]):
                    print(" ", end="")
                    elems.append(" ")
                for j in range(self.__size):
                    print("#", end="")
                    elems.append("#")
                print()
                elems.append("\n")
        return elems

    def __str__(self):
        """Prints the current square using #'s"""

        elems = []
        if self.__size == 0:
            elems.append("\n")
        else:
            for y in range(self._position[1]):
                elems.append("\n")
            for i in range(self.__size):
                for x in range(self._position[0]):
                    elems.append(" ")
                for j in range(self.__size):
                    elems.append("#")
                elems.append("\n")

        return "".join(elems[:-1])

    @property
    def position(self):
        """Retrieves the co-ordinates of the current square"""

        return self._position

    @position.setter
    def position(self, value):
        """Sets the co-ordinates of the current square"""

        message = "position must be a tuple of 2 positive integers"
        if len(value) != 2:
            raise TypeError(message)
        for item in value:
            if type(item) is not int or item < 0:
                raise TypeError(message)

        self._position = value
