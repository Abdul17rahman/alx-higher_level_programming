#!/usr/bin/python3
"""
    Base Class Test Module
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
        Testing functions in the Base class

        Args:
            unittest - Testing module

        Methods:
            setup - Settup the instances to use
            test_init - Tests the Initialization
    """
    def setUp(self):
        """ Sets up an instance to use for testing"""
        self.b1 = Base()
        self.b4 = Base(12)

    def test_init(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b4.id, 12)

    def test_valid_input(self):
        with self.assertRaises(TypeError):
            self.b1.valid_input("width", "hello", "dime")
        with self.assertRaises(ValueError):
            self.b1.valid_input("width", -1, "dime")
        with self.assertRaises(ValueError):
            self.b1.valid_input("height", 0, "dime")
        with self.assertRaises(TypeError):
            self.b1.valid_input("x", "hello")
        with self.assertRaises(ValueError):
            self.b1.valid_input("y", -1)
