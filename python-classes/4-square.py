#!/usr/bin/python3
"""

This module is to create a square
"""


class Square:

    """

    This is a class to calculate the square
    """

    def __init__(self, size=0):

        """
        initiates the constructor with optional size = 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):

        """
        getter to be able to access the private instance
        """

        return self.__size

    @size.setter
    def size(self, value):

        """
        Setter method to set the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def area(self):

        """
        calculating the area
        """

        return self.__size ** 2
