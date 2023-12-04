#!/usr/bin/python3
"""_summary_"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """_summary_"""

    def __init__(self, size):
        """_summary_"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
