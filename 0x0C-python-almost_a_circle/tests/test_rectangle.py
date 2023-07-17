#!/usr/bin/python3
""" Reactangle Test Module"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        Testing the Rect methods

            Methods:
                setUp - Sets up the Rect instances
                test_init - Tests the initialization
                test_width - Tests width getter and setter
                test_height - Tests height getter and setter
                test_x - Tests the getter and setter of x
                test_y - Tests the getter and setter of y
    """
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(10, 2, 0, 0, 12)
        self.r3 = Rectangle(8, 7, 3, 5)

    def test_init(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r2.id, 12)

        with self.assertRaises(TypeError):
            r = Rectangle("3", 1, 0, 0)
        with self.assertRaises(TypeError):
            r = Rectangle(2, "1", 0, 0)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 1, "0", 0)
        with self.assertRaises(TypeError):
            r = Rectangle(2, 1, 0, "0")

        with self.assertRaises(ValueError):
            r = Rectangle(0, 1, 0, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0, 0, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 1, 0, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -1, 0, 0)

    def test_width(self):
        self.assertEqual(self.r3.width, 8)

        self.r1.width = 4
        self.r3.width = 6

        self.assertEqual(self.r1.width, 4)
        self.assertEqual(self.r3.width, 6)

        with self.assertRaises(TypeError):
            self.r3.width = "hello"
        with self.assertRaises(ValueError):
            self.r3.width = 0
        with self.assertRaises(ValueError):
            self.r3.width = -1

    def test_height(self):
        self.assertEqual(self.r3.height, 7)

        self.r1.height = 6
        self.r3.height = 8

        self.assertEqual(self.r1.height, 6)
        self.assertEqual(self.r3.height, 8)

        with self.assertRaises(TypeError):
            self.r3.height = "hello"
        with self.assertRaises(ValueError):
            self.r3.height = 0
        with self.assertRaises(ValueError):
            self.r3.height = -1

    def test_x(self):
        self.assertEqual(self.r3.x, 3)

        self.r1.x = 2
        self.r3.x = 4

        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r3.x, 4)

        with self.assertRaises(TypeError):
            self.r3.x = "hello"
        with self.assertRaises(ValueError):
            self.r3.x = -1

    def test_y(self):
        self.assertEqual(self.r3.y, 5)

        self.r1.y = 1
        self.r3.y = 6

        self.assertEqual(self.r1.y, 1)
        self.assertEqual(self.r3.y, 6)

        with self.assertRaises(TypeError):
            self.r3.y = "hello"
        with self.assertRaises(ValueError):
            self.r3.y = -1

    def test_area(self):
        self.assertEqual(self.r1.area(), 20)

    def test_str(self):
        self.assertEqual(str(self.r2), "[Rectangle] (12) 0/0 - 10/2")

    def test_update(self):
        pass
