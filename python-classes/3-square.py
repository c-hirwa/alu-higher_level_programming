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

    def area(self):

        """
        calculating the area
        """

        return self.__size ** 2
