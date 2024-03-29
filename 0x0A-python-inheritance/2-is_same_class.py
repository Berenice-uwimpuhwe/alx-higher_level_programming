#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class"""
    if type(obj) == a_class:
        return True
    return False
