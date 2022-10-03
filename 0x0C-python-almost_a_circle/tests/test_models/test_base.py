#!/usr/python3
'''
File: test_base.py
Classes:
-> test_constructor
-> test_inheritance
-> test_to_json
-> test_from_json
-> test_create
->
'''
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_constructor(unittest.TestCase):
    ''' tests for Base Class Constructor Method '''

    def setUp(self):
        ''' Set up for all methods '''
        Base._Base__nb_objects = 0

    def test_no_args(self):
        ''' no arguments passed '''
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_none_auti(self):
        ''' None as argument '''
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_id_normal(self):
        ''' int arguments - id assignment'''
        obj1 = Base(1)
        self.assertEqual(obj1.id, 1)
        obj0 = Base(None)
        self.assertEqual(obj0.id, 1)
        obj2 = Base(-2)
        self.assertEqual(obj2.id, -2)
        obj_2 = Base()
        self.assertEqual(obj_2.id, 2)
        obj3 = Base(100)
        self.assertEqual(obj3.id, 100)
        obj4 = Base(1024)
        self.assertEqual(obj4.id, 1024)

    def test_private_attr(self):
        ''' Check private __nb_objects attr '''
        obj = Base()
        with self.assertRaises(AttributeError):
            obj.__nb_objects


class test_inheritance(unittest.TestCase):
    ''' tests for inheritance and types'''

    def test_type(self):
        ''' object created is instance '''
        obj = Base(1)
        self.assertTrue(isinstance(obj, Base))

    def test_r_is_base(self):
        ''' rectangle is base instance '''
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertTrue(isinstance(r, Base))

    def test_s_is_base(self):
        ''' square is base instance '''
        s = Rectangle(1, 1, 1, 1)
        self.assertTrue(isinstance(s, Base))


class test_to_json(unittest.TestCase):
    ''' tests for to_json_string method'''

    def test_no_args(self):
        ''' no arguments passed '''
        with self.assertRaises(TypeError):
            self.assertEqual(Base.to_json_string(), '[]')

    def test_none(self):
        ''' None as argument '''
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_empty_list(self):
        ''' empty list [] '''
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_empty_dict(self):
        ''' list with empty dict [{}] '''
        self.assertEqual(Base.to_json_string([{}]), '[{}]')

    def test_normal(self):
        ''' list and dictonaries normally '''
        objs = [
            {'id': 1, 'width': 3, 'height': 1},
            {'id': 2, 'width': 4, 'height': 4, 'x': 2, 'y': 2},
            {'id': 3}
        ]
        jsonify = Base.to_json_string(objs)
        self.assertEqual(json.loads(jsonify), objs)

    def test_normal_rectangle(self):
        ''' rectangles to json '''
        r = Rectangle(3, 4, 10, 10)
        r1 = Rectangle(5, 1)
        check = [r.to_dictionary(), r1.to_dictionary()]
        jsonify = Base.to_json_string(check)
        self.assertEqual(json.loads(jsonify), check)

    def test_normal_square(self):
        ''' squares to json '''
        s = Square(2, 2, 2)
        s1 = Square(5)
        check = [s.to_dictionary(), s1.to_dictionary()]
        jsonify = Base.to_json_string(check)
        self.assertEqual(json.loads(jsonify), check)

    def test_return_type(self):
        ''' to_json_string must return str '''
        objs = [
            {'id': 2, 'width': 4, 'height': 4, 'x': 2, 'y': 2}
        ]
        jsonify = Base.to_json_string(objs)
        self.assertEqual(type(jsonify), str)


class test_from_json(unittest.TestCase):
    ''' tests for from_json_string method'''

    def test_no_args(self):
        ''' no arguments passed '''
        with self.assertRaises(TypeError):
            self.assertEqual(Base.from_json_string(), '[]')

    def test_none(self):
        ''' None as argument '''
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_str(self):
        ''' empty json string '''
        self.assertEqual(Base.from_json_string(''), [])

    def test_empty_list(self):
        ''' json empty list [] '''
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_empty_dict(self):
        ''' json list with empty dict [{}] '''
        self.assertEqual(Base.from_json_string('[{}]'), [{}])

    def test_normal(self):
        ''' list and dictonaries normally '''
        init = '''[
            {"id": 1, "width": 3, "height": 1},
            {"id": 2, "width": 4, "height": 4, "x": 2, "y": 2},
            {"id": 3}
        ]'''
        check = [
            {'id': 1, 'width': 3, 'height': 1},
            {'id': 2, 'width': 4, 'height': 4, 'x': 2, 'y': 2},
            {'id': 3}
        ]
        self.assertEqual(Base.from_json_string(init), check)

    def test_normal_rectangle(self):
        ''' rectangles to json '''
        init = '''[
            {"id": 1, "width": 3, "height": 4, "x": 10, "y": 10},
            {"id": 6, "width": 5, "height": 1, "x": 0, "y": 0}
        ]'''
        r = Rectangle(3, 4, 10, 10, 1)
        r1 = Rectangle(5, 1)
        check = [r.to_dictionary(), r1.to_dictionary()]
        self.assertEqual(Base.from_json_string(init), check)

    def test_normal_square(self):
        ''' squares to json '''
        init = '''[
            {"id": 10, "size": 2, "x": 2, "y": 2},
            {"id": 7, "size": 5, "x": 0, "y": 0}
        ]'''
        s = Square(2, 2, 2, 10)
        s1 = Square(5)
        check = [s.to_dictionary(), s1.to_dictionary()]
        self.assertEqual(Base.from_json_string(init), check)

    def test_return_type(self):
        ''' to_json_string must return str '''
        init = '[{"id": 1, "size": 3}]'
        check = [{'id': 1, 'size': 3}]
        tp = Base.from_json_string(init)
        self.assertEqual(tp, check)
        self.assertTrue(type(tp), list)
        self.assertTrue(type(tp[0]), dict)


class test_create(unittest.TestCase):
    ''' test for create method '''

    def test_rectangles(self):
        ''' Rectangle instances '''
        r = Rectangle(3, 4, 10, 10)
        check = Rectangle.create(**r.to_dictionary())
        self.assertFalse(r is check)
        self.assertFalse(r == check)


    def test_squares(self):
        ''' Squares instances '''
        r = Square(5)
        check = Rectangle.create(**r.to_dictionary())
        self.assertFalse(r is check)
        self.assertFalse(r == check)
