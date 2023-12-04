#!/usr/bin/python3
"""_summary_
"""


class MyList(list):
    """Class that contains list

    Args:
        list (int): list
    """

    def print_sorted(self):
        """print ascending sorted list
        """
        print(sorted(self))
