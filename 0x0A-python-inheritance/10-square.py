#!/usr/bin/python3
""" 0x0A. 10-square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle and thus from BaseGeometry, for use with
    rectangular constructs of equal sides.

    Args:
        size (int): length of side of square

    Attributes:
        __size (int): length of side of square

    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method to calculate the area of a square.

        This method calculates the area of a square by multiplying the length of its side by itself.

        Attributes:
            __size (int): Length of the side of the square.

        Returns:
            The square of the length of the side (__size ** 2).
        """

        return self.__size ** 2
