The ``7-base_geometry`` module
============================

Using ``BaseGeometry``
---------------------

Import function from module:
    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry

Correct Class Type test:
    >>> bg = BaseGeometry()
    >>> type(bg) == BaseGeometry
    True


area() instance method
----------------------
area method is an instance method:
    >>> type(BaseGeometry.__dict__['area'])
    <class 'function'>

area method called via class with no args:
    >>> bg.__class__.area()
    Traceback (most recent call last):
    TypeError: area() missing 1 required positional argument: 'self'

area method args test (1 arg):
    >>> bg.area(10)
    Traceback (most recent call last):
    TypeError: area() takes 1 positional argument but 2 were given

area method normal test:
    >>> bg.area()
    Traceback (most recent call last):
    Exception: area() is not implemented


integer_validator() instance method
-----------------------------------
integer_validator is an instance method:
    >>> type(BaseGeometry.__dict__['integer_validator'])
    <class 'function'>

integer_validator method called via class with no args:
    >>> bg.__class__.integer_validator()
    Traceback (most recent call last):
    TypeError: integer_validator() missing 3 required positional arguments: 'self', 'name', and 'value'

integer_validator method arg test (0 args):
    >>> bg.integer_validator()
    Traceback (most recent call last):
    TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'
    
integer_validator method arg test (3 args):
    >>> bg.integer_validator(1, 1, 1)
    Traceback (most recent call last):
    TypeError: integer_validator() takes 3 positional arguments but 4 were given

integer_validator method float.0 value:
    >>> bg.integer_validator("foo", 3.0)
    Traceback (most recent call last):
    TypeError: foo must be an integer

integer_validator method float.x value:
    >>> bg.integer_validator("arg", 3.14)
    Traceback (most recent call last):
    TypeError: arg must be an integer

integer_validator method string value:
    >>> bg.integer_validator("Bar", "bar")
    Traceback (most recent call last):
    TypeError: Bar must be an integer

integer_validator method bool value:
    >>> bg.integer_validator("zar", True)
    Traceback (most recent call last):
    TypeError: zar must be an integer

integer_validator method list value:
    >>> bg.integer_validator("a", [1])
    Traceback (most recent call last):
    TypeError: a must be an integer

integer_validator method None value:
    >>> bg.integer_validator("foo", None)
    Traceback (most recent call last):
    TypeError: foo must be an integer

integer_validator method 0 value:
    >>> bg.integer_validator("key", 0)
    Traceback (most recent call last):
    ValueError: key must be greater than 0

integer_validator method negative value:
    >>> bg.integer_validator("key", -1000)
    Traceback (most recent call last):
    ValueError: key must be greater than 0

integer_validator method ok value:
    >>> bg.integer_validator("key", 98)
    
integer_validator method ok value 2:
    >>> bg.integer_validator("key", 1)

integer_validator method empty string:
    >>> bg.integer_validator("", 1)

integer_validator method empty string:
    >>> bg.integer_validator(None, 1)

integer_validator method tuple:
    >>> bg.integer_validator("Foo", (1, 2))
    Traceback (most recent call last):
    TypeError: Foo must be an integer

integer_validator method dic:
    >>> bg.integer_validator("Foo", {1, 2})
    Traceback (most recent call last):
    TypeError: Foo must be an integer
