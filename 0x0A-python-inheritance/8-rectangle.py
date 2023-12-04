#!/usr/bin/python3
"""summary"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """inherits from BaseGeometry"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
