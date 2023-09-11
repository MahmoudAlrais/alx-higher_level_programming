#!/usr/bin/python3
"""Return instance of specific class."""


def is_same_class(obj, a_class):
    """Check if object is instance of  given class.
    Args:
        obj (any): object to check.
        a_class (type): class to compare type of obj to.
    Returns:
        Boolean of instance of a_class.
    """
    if type(obj) == a_class:
        return True
    return False
