#!/usr/bin/python3
"""
Defines unit tests for the Place class
"""
from unittest import TestCase
from datetime import datetime
from models.place import Place


class TestPlace(TestCase):
    """
    Test class with methods testing the Place class
    """

    def test_new_instance(self):
        """ Test the creation of Place instance """
        obj = Place()
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])
