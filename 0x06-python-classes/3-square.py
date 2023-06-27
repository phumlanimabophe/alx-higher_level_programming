class Square:
    """Class defined for square generation.

    Attributes:
        __size (int): length of one side of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The length of one side of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (length of one side squared).
        """
        return self.__size ** 2
