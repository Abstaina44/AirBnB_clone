#!/usr/bin/python3
"""
Defines unit tests for the User class
"""
from unittest import TestCase
from datetime import datetime
from models.user import User
from os.path import isfile


class TestUser(TestCase):
    """
    Test class with methods testing the User class
    """

    def test_new_instance(self):
        """ Test the creation of User instance """
        obj = User()
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")
