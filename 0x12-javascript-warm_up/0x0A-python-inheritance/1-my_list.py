#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """
    A class (MyList) subset of list
    """

    def print_sorted(self):
        """
        A method that prints a list in asscending sort.
        """

        print(sorted(self.copy()))


