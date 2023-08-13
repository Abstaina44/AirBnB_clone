#!/usr/bin/python3
"""
Defines unit tests for the Amenity class
"""
from unittest import TestCase
from datetime import datetime
from models.base_model import BaseModel
from os.path import isfile


class TestBaseModel(TestCase):
    """
    Test class with methods testing the Amenity class
    """

    def test_save(self):
        """ Test the save method """
        obj = BaseModel()
        updated_at = datetime.now()
        first_update = obj.updated_at
        # Compare before calling save
        self.assertEqual(obj.updated_at.date(), updated_at.date())
        obj.save()
        updated_at = datetime.now()
        second_update = obj.updated_at
        # Compare after calling save
        self.assertEqual(obj.updated_at.date(), updated_at.date())
        self.assertTrue(isfile("file.json"))
        self.assertLess(first_update, second_update, "Error")

    def test_to_dict(self):
        """ Test the to_dict method """
        expected = ("id", "created_at", "updated_at", "__class__")
        obj = BaseModel()
        actual = obj.to_dict()
        self.assertEqual(sorted(tuple(actual.keys())), sorted(expected))
