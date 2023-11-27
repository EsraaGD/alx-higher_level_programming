#!/usr/bin/python3
"""This module defines a rectangle with private attributes width and height.
"""


class Rectangle:
    """Represetns a rectangle
    """

    def __init__(self, width=0, height=0):
        """Initalize a rec instance

        Args:
            width (int): Width of rec. Defaults to 0.
            height (int): Height of rec. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute

        Returns:
            int: width of rec
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute

        Args:
            value (int): width to set

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute

        Returns:
            int: height of rec
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute

        Args:
            value (int): height to set

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value > 0:
            raise ValueError("height must be >= 0")
        self.__height = value
