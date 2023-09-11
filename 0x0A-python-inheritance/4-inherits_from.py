#!/usr/bin/python3
"""Defines inherited class-checking method."""


def inherits_from(obj, a_class):
    """Checks if object is inherited instance of a class.
    Args:
        obj (any): object to check.
        a_class (type): class to compare.
    Returns:
        A boolean of inheritance.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
