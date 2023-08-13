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
        # Compare before calling save
        self.assertEqual(obj.updated_at.date(), updated_at.date())
        obj.save()
        updated_at = datetime.now()
        # Compare after calling save
        self.assertEqual(obj.updated_at.date(), updated_at.date())
        self.assertTrue(isfile("file.json"))

    def test_to_dict(self):
        """ Test the to_dict method """
        expected = ("id", "created_at", "updated_at", "__class__")
        obj = BaseModel()
        actual = obj.to_dict()
        self.assertEqual(sorted(tuple(actual.keys())), sorted(expected))

    def test_obj_with_kwargs_to_dict(self):
        """
        Test the to_dict method for BaseModel object
        created with key-worded arguments
        """
        expected = ("id", "created_at", "updated_at", "__class__", "name")
        obj = BaseModel(**{"id": "398c7f36-10a2-4b69-9e28-d9ccf0dbde37",
                        "created_at": datetime.now().isoformat(),
                        "updated_at": datetime.now().isoformat(),
                        "name": "Jake Savage"})
        self.assertEqual(sorted(tuple(obj.to_dict().keys())), sorted(expected))

    def test_str(self):
        """ Test the __str__ method """
        obj = BaseModel()
        id = obj.id
        self.assertEqual(str(obj), f"[BaseModel] ({id}) {obj.__dict__}")
