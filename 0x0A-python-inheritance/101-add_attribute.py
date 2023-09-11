#!/usr/bin/python3
"""Define a function attributes."""


def add_attribute(obj, att, value):
    """Add new attribute to object if possible.
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
