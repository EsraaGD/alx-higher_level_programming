#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): Size of the square
            x (int, optional): Initialize a new Square instance. Defaults to 0.
            y (int, optional): Y-coordinate of the square. Defaults to 0.
            id (_type_, optional): Identifier for the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): Size value
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args: Variable number of arguments.
            **kwargs: Variable number of keyword arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square.

        Returns:
            dict: Dictionary representation of the square.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
