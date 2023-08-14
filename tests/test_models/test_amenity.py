#!/usr/bin/python3
"""
Defines unit tests for the Amenity class
"""
from unittest import TestCase
from datetime import datetime
from models.amenity import Amenity


class TestUser(TestCase):
    """
    Test class with methods testing the Amenity class
    """

    def test_new_instance(self):
        """ Test the creation of Amenity instance """
        obj = Amenity()
        self.assertEqual(obj.name, "")
