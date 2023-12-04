#!/usr/bin/python3
"""_summary_"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """_summary_"""

    def __init__(self, width, height):
        """Init rec with given width and height

        Args:
            width (int): width of rec
            height (int): height of rec
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
