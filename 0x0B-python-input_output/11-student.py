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

    def to_json(self, attrs=None):
        ''' Method that returns directory description with filter '''
        res = {}
        if attrs:
            for attr in attrs:
                if attr in self.__dict__:
                    res[attr] = self.__dict__[attr]
        else:
            for attr in self.__dict__:
                res[attr] = self.__dict__[attr]

        return res

    def reload_from_json(self, json):
        ''' Replaces all attributes of the Student instance '''
        for attr in json:
            self.__dict__[attr] = json[attr]
