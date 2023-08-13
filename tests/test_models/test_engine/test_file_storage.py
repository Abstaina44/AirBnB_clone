#!/usr/bin/python3
"""
Defines unit tests for the File Storage class.
"""
from unittest import TestCase
from uuid import uuid4
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):
    """
    Test class with methods testing the File Storage
    class
    """

    def test_reload(self):
        """ Test the reload method """
        obj = FileStorage()
        objects = obj.all()
        self.assertTrue(len(objects) > 0)
