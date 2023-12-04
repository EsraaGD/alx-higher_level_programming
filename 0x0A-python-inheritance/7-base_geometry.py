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
        if type(value) is not (int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
