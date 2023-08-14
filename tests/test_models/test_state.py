#!/usr/bin/python3
"""
Defines unit tests for the State class
"""
from unittest import TestCase
from datetime import datetime
from models.state import State


class TestState(TestCase):
    """
    Test class with methods testing the State class
    """

    def test_new_instance(self):
        """ Test the creation of State instance """
        obj = State()
        self.assertEqual(obj.name, "")
