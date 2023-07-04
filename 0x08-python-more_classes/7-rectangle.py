#!/usr/bin/python3
"""Module 7-rectangle
"""


class Rectangle:
    """Rectangle class defination.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes Rectangle instance in contructor.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns informal string representation
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rectangle_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += str(self.print_symbol)
            rectangle_str += '\n'
        return rectangle_str[:-1]

    def __repr__(self):
        """Return internal string representation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Fire when rectangle instance is destroyed."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves width of Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height of Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of Rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of Rectangle instance
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
