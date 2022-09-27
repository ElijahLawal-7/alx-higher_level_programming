#!/usr/bin/python3
'''
file: 11-student.py
Classes:
-> Student
'''


class Student:
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Constructor method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Method that returns directory description '''
        return self.__dict__.copy()
