#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """Represent student."""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student.

        Args:
            first_name (str): The first name of student.
            last_name (str): The last name of student.
            age (int): The age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of Student.

        If attrs is a list of strings, represents only those attributes
        included in list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
