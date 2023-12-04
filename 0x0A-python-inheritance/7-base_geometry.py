#!/usr/bin/python3
"""_summary_"""


class BaseGeometry():
    """empty"""

    def area(self):
        """Area not implemeted

        Raises:
            Exception: Area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value integer and is > 0

        Args:
            name (str): name of value
            value: value to be validated

        Raises:
            TypeError: name must be integer
            ValueError: name must be greater than 0
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
