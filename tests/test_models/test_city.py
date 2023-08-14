#!/usr/bin/python3
"""
Defines unit tests for the City class
"""
from unittest import TestCase
from datetime import datetime
from models.city import City


class TestCity(TestCase):
    """
    Test class with methods testing the City class
    """

    def test_new_instance(self):
        """ Test the creation of City instance """
        obj = City()
        self.assertEqual(obj.state_id, "")
        self.assertEqual(obj.name, "")
