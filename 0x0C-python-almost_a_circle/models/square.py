#!/usr/bin/python3
"""0x0C. Python - Almost a circle, task 10 - 14"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Creates square objects with 2 dimensions and offset coordinates.

    Inherits from the Rectangle class and sets the size as an alias for width and height.

    Args:
        size (int): The size of the square.
        x (int): The horizontal offset of the square.
        y (int): The vertical offset of the square.
        id (int): The unique identifier for each instance of the class.

    Project task:
        10. And now, the Square! - class Square `__init__`, `__str__`,
            only inherited validation, no new attributes
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: A string in the format '[Square] (<id>) <x>/<y> - <size>'.

        Project task:
            10. And now, the Square! - class Square `__init__`, `__str__`,
                only inherited validation, no new attributes
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """The size of the square.

        Returns:
            int: The size of the square.

        Project task:
            11. Square size - public getter and setter `size`, using
                validation from super().width
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Project task:
            11. Square size - public getter and setter `size`, using
                validation from super().width
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the square.

        Args:
            *args: Non-keyword arguments in the order of appearance: id, size, x, y.
            **kwargs: Keyword arguments to update the attributes.

        Raises:
            TypeError: If the number of arguments is not between 1 and 4.
            KeyError: If an invalid attribute name is provided.

        Project tasks:
            12. Square update - updates `id`, `size`, `x`, or `y` based on *args or **kwargs.

        """
        if len(args) > 4 or len(kwargs) > 4:
            raise TypeError("Square.update() takes 1 to 4 keyword or non-keyword arguments")

        if args:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
                if attributes[i] == "id":
                    Base._Base__assigned_ids.add(value)
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    Base._Base__assigned_ids.add(value)
                elif key in ("size", "x", "y"):
                    setattr(self, key, value)
                else:
                    raise KeyError(f"Invalid attribute name: {key}")

    def to_dictionary(self):
        """Returns a dictionary representation of the square.

        Returns:
            dict: A dictionary containing the attribute names and their values.

        Project tasks:
            14. Square instance to dictionary representation
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
