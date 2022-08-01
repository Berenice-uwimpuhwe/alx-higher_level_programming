#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """inherits from list public instance method"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
