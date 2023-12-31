#!/usr/bin/python3
"""This module defines a rectangle with private attributes width and height.
    """


class Rectangle:
    """Represetns a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

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
        elif value < 0:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """Initalize a rec instance

        Args:
        width (int): Width of rec. Defaults to 0.
        height (int): Height of rec. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Find area of rec

        Returns:
            int: area of rec
        """
        return self.__width * self.__height

    def perimeter(self):
        """Find perimeter of rec

        Returns:
            int: perimeter of rec
        """
        if self.__width == 0 and self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Return a string representation of the rec

        Returns:
            str: string of rec
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.__width] * self.__height
        )

    def __repr__(self):
        """String representation of rec

        Returns:
            str: String representation of rec
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Detect deletion of rec
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return biggest area rec

        Args:
            rect_1 (rectangle): instance 1 of rec
            rect_2 (rectangle): instance 2 of rec

        Raises:
            TypeError: If rect_1 is not an inst of rec
            TypeError: If rect_2 is not an inst of rec

        Returns:
            Rectangle: Rec with biggest area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rec instance with equal width & height(a square)

        Args:
            size (int): size of square. Defaults to 0.

        Returns:
            Rectangle: new instance that's a square
        """
        return cls(width=size, height=size)
