#!/usr/bin/python3
"""_summary_"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry():
    """Empty"""

    def area(self):
        """area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """_summary_

                Args:
                        name (_type_): _description_
                        value (_type_): _description_

                Raises:
                        TypeError: _description_
                        ValueError: _description_
                """
        if type(value) is not (int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """inherits from BaseGeometry"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self) -> str:
        """string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
