#!/usr/bin/python3
"""
Defines unit tests for the Review class
"""
from unittest import TestCase
from datetime import datetime
from models.review import Review


class TestReview(TestCase):
    """
    Test class with methods testing the Review class
    """

    def test_init(self):
        """ Test review object creation """
        created_at = datetime.now()
        obj = Review()
        self.assertEqual(obj.created_at.date(), created_at.date())

    def test_str(self):
        """ Test the __str__ method """
        created_at = datetime.now()
        updated_at = datetime.now()
        obj = Review()
        actual = str(obj)
        self.assertIs(type(actual), str)
        self.assertEqual(obj.created_at.date(), created_at.date())
        self.assertEqual(obj.updated_at.date(), updated_at.date())

    def test_save(self):
        """ Test the save method """
        obj = Review()
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
        obj = Review()
        actual = obj.to_dict()
        self.assertEqual(sorted(tuple(actual.keys())), sorted(expected))
