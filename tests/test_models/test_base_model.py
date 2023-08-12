#!/usr/bin/env python3
"""
Defines unit tests for the Base Model class.
"""
from unittest import TestCase
from uuid import uuid4
from datetime import datetime, date
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """
    Test class with methods testing the Base Class
    """

    def test_init_without_args(self):
        """ Test object creation without any arguments """
        created_at = datetime.now()
        updated_at = datetime.now()
        obj = BaseModel()
        self.assertEqual(obj.created_at.date(), created_at.date())
        self.assertEqual(obj.updated_at.date(), created_at.date())

    def test_init_with_args(self):
        """ Test object creation with key-worded arguments """
        create = date(2000, 12, 31).isoformat()
        update = date(2001, 1, 1).isoformat()
        id = "60efac0e-85aa-47e0-91e1-dfb0daafacc6"
        obj_dict = {"id": id, "created_at": create, "updated_at": update}
        obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, id)
        self.assertEqual(obj.created_at, datetime.fromisoformat(create))
        self.assertEqual(obj.updated_at, datetime.fromisoformat(update))

    def test_str(self):
        """ Test the __str__ method """
        id = uuid4()
        created_at = datetime.now()
        updated_at = datetime.now()
        obj = BaseModel()
        actual = str(obj)
        self.assertIs(type(actual), str)
        self.assertEqual(obj.created_at.date(), created_at.date())
        self.assertEqual(obj.updated_at.date(), updated_at.date())

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

    def test_to_dict(self):
        """ Test the to_dict method """
        expected = ("id", "created_at", "updated_at", "__class__")
        obj = BaseModel()
        actual = obj.to_dict()
        self.assertEqual(sorted(tuple(actual.keys())), sorted(expected))
