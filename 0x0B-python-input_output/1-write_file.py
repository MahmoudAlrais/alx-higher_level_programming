#!/usr/bin/python3
"""Defines file-writing function."""


def write_file(filename="", text=""):
    """Write string to  UTF8 text file.

    Args:
        filename (str): The name of file to write.
        text (str):  text to write to file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
