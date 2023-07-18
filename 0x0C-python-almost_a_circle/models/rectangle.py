#!/usr/bin/python3
"""0x0C. Python - Almost a circle, task 2 - 13"""
from models.base import Base


class Rectangle(Base):
    """Creates rectangle objects with 2 dimensions and offset coordinates.

    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): Horizontal offset of the rectangle.
        y (int): Vertical offset of the rectangle.
        id (int): Unique identifier for each instance.

    Project tasks:
        2. First Rectangle - __init__, getters and setters for `width`, `height`, `x`, `y`
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the `Rectangle` class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): Horizontal offset of the rectangle.
            y (int): Vertical offset of the rectangle.
            id (int): Unique identifier for the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __integer_validator(self, attr, value):
        """
        Validates incoming argument values for use with internal attributes.

        Args:
            attr (str): Name of the intended attribute assignment.
            value (any): Expecting an int, but will filter out other types.

        Raises:
            TypeError: If any incoming value is not an int.
            ValueError: If any `width` or `height` candidate is <= 0, or if `x` or `y` candidates are < 0.

        Project task:
            3. Validate attributes - input validation for `width`, `height`, `x`, `y`
        """
        if not isinstance(value, int):
            raise TypeError(f"{attr} must be an integer")
        if attr in ("width", "height"):
            if value <= 0:
                raise ValueError(f"{attr} must be > 0")
        elif attr in ("x", "y"):
            if value < 0:
                raise ValueError(f"{attr} must be >= 0")

    @property
    def width(self):
        """Getter for the `width` attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the `width` attribute.

        Args:
            value (int): Width of the rectangle.

        Attributes:
            __width (int): Width of the rectangle.
        """
        self.__integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for the `height` attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the `height` attribute.

        Args:
            value (int): Height of the rectangle.

        Attributes:
            __height (int): Height of the rectangle.
        """
        self.__integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for the `x` attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the `x` attribute.

        Args:
            value (int): Horizontal offset of the rectangle.

        Attributes:
            __x (int): Horizontal offset of the rectangle.
        """
        self.__integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for the `y` attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the `y` attribute.

        Args:
            value (int): Vertical offset of the rectangle.

        Attributes:
            __y (int): Vertical offset of the rectangle.
        """
        self.__integer_validator("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle as the product of `width` and `height`.

        Returns:
            int: The area of the rectangle.

        Project tasks:
            4. Area first - public method `area()`
        """
        return self.width * self.height

    def display(self):
        """Prints a representation of the rectangle to stdout using '#'.

        Project tasks:
            5. Display #0 - public method `display()`, only use `width` and `height`
            7. Display #1 - include use of offset vars `x` and `y`
        """
        display = ""
        for _ in range(self.y):
            display += "\n"
        for _ in range(self.height):
            for _ in range(self.x):
                display += " "
            for _ in range(self.width):
                display += "#"
            if _ < self.height - 1:
                display += "\n"
        self.__display = display
        print(display)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string in the format '[Rectangle] (<id>) <x>/<y> - <width>/<height>'.

        Project tasks:
            6. __str__ - `__str__` method
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle.

        Args:
            *args: Non-keyword arguments in the order of appearance: id, width, height, x, y.
            **kwargs: Keyword arguments to update the attributes.

        Raises:
            TypeError: If the number of arguments is not between 1 and 5.
            KeyError: If an invalid attribute name is provided.

        Project tasks:
            8. Update #0 - updates `id`, `width`, `height`, `x`, or `y` based on the number of args using *args.
            9. Update #1 - adds support for **kwargs to access key-worded arguments in any order. If *args is not empty, **kwargs is skipped.
        """
        if len(args) > 5 or len(kwargs) > 5:
            raise TypeError("Rectangle.update() takes 1 to 5 keyword or non-keyword arguments")

        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
                if attributes[i] == "id":
                    Base._Base__assigned_ids.add(value)
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    Base._Base__assigned_ids.add(value)
                elif key in ("width", "height", "x", "y"):
                    setattr(self, key, value)
                else:
                    raise KeyError(f"Invalid attribute name: {key}")

    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle.

        Returns:
            dict: A dictionary containing the attribute names and their values.

        Project tasks:
            13. Rectangle instance to dictionary representation
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
