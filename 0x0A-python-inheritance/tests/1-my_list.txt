The ``1-my_list`` module
============================

Using ``1-mylist``
---------------------

Import function from module:
    >>> MyList = __import__('1-my_list').MyList

Correct Class Type test:
    >>> ml = MyList()
    >>> type(ml) == MyList
    True

Correct Instance test:
    >>> ml = MyList()
    >>> isinstance(ml, list)
    True

print_sorted method is an instance method:
    >>> type(MyList.__dict__['print_sorted'])
    <class 'function'>

print_sorted method called via class with no args:
    >>> ml.__class__.print_sorted()
    Traceback (most recent call last):
    TypeError: print_sorted() missing 1 required positional argument: 'self'

print_sorted method called with 1 arg:
    >>> ml.print_sorted([4, 2, 5])
    Traceback (most recent call last):
    TypeError: print_sorted() takes 1 positional argument but 2 were given

print_sorted method called with 2 args:
    >>> ml.print_sorted([4, 2, 5], 1)
    Traceback (most recent call last):
    TypeError: print_sorted() takes 1 positional argument but 3 were given

Empty list test:
    >>> ml = MyList()
    >>> ml.print_sorted()
    []

Normal list test:
    >>> ml = MyList([2, 10, 1])
    >>> ml.print_sorted()
    [1, 2, 10]

Normal list test 2:
    >>> ml = MyList([1, 4, 2, 3, 5])
    >>> ml.print_sorted()
    [1, 2, 3, 4, 5]

Negative ints list test:
    >>> ml = MyList([-1000, -98, -232565, 0, -23423434, -123])
    >>> ml.print_sorted()
    [-23423434, -232565, -1000, -123, -98, 0]

Original list unchanged:
    >>> ml = MyList([2, 10, 1, -10, 20, 100, 0])
    >>> ml.print_sorted()
    [-10, 0, 1, 2, 10, 20, 100]
    >>> ml
    [2, 10, 1, -10, 20, 100, 0]

List already in order:
    >>> ml = MyList([-10, 0, 1, 2, 10, 20, 100])
    >>> ml.print_sorted()
    [-10, 0, 1, 2, 10, 20, 100]

Test append:
    >>> ml = MyList()
    >>> ml.append(10)
    >>> ml
    [10]
