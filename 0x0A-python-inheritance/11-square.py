#!/usr/bin/python3
""" 0x0A. 11-square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle and BaseGeometry.

    This class is designed for representing squares, which are rectangular constructs with equal sides.

    Args:
        size (int): Length of the side of the square.

    Attributes:
        __size (int): Length of the side of the square.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method to calculate the area of a square, invoking Rectangle's area method.

        This method calculates the area of a square by multiplying the length of its side by itself. It invokes the `Rectangle` class's `area` method for the calculation.

        Attributes:
            __size (int): Length of the side of the square.

        Returns:
            The square of the length of the side (__size ** 2).
        """

        return self.__size ** 2

    def __str__(self):
        """ Provides printable representation of Square object.

        """
        return '[Square] {}/{}'.format(self.__size, self.__size)
