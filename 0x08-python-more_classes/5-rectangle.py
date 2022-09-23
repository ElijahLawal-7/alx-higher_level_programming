#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """
    Rectangle that defines a rectangle by:
    Private instance attribute: width (int)
    Private instance attribute: height (int)
    Instantiation with optional width and height
    Public instance method: def area(self)
    Public instance method: def perimeter(self)
    print() and str() should print the rectangle with the character #
    repr() should return a string representation of the rectangle
     to be able to recreate a new instance by using eval()
    deconstructor method implemented 'Bye rectangle...'
    """

    def __init__(self, width=0, height=0):
        """ Constructor method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter width property """
        return self.__width

    @property
    def height(self):
        """ getter height property """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter width property """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter height property """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Return area of rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Return perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ Return string to print rectangle with # """
        if self.width == 0 or self.height == 0:
            return ''
        to_print = ''
        for col in range(self.height):
            for row in range(self.width):
                to_print += '#'
            if col != self.height - 1:
                to_print += '\n'
        return to_print

    def __repr__(self):
        """ Return a string representation of the rectangle """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ Deconstructor method """
        print("Bye rectangle...")
