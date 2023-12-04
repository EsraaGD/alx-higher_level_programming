#!/usr/bin/python3
"""_summary_"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
