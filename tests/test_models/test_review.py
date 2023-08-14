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

    def test_new_instance(self):
        """ Test the creation of Review instance """
        obj = Review()
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")
