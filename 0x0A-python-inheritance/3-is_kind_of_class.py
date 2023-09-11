#!/usr/bin/python3
"""A class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if object is instance or inherited instance of class.
    Args:
        obj (any): object to check.
        a_class (type): class to compare the type of obj to.
    Returns:
        Boolean of instance.
    """
    if isinstance(obj, a_class):
        return True
    return False
