#!/usr/bin/env python3
"""
Defines unit tests for the File Storage class.
"""
from unittest import TestCase
from uuid import uuid4
from datetime import datetime, date
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os.path import isfile


class TestFileStorage(TestCase):
    """
    Test class with methods testing the File Storage
    class
    """
    def test_all(self):
        """ Test the all method """
        obj = FileStorage()
        actual_obj = obj.all()
        self.assertIs(type(actual_obj), dict)

    def test_new(self):
        """ Test the new method """
        my_dict = {"id": "b29b5df5-72e7-43af-8b10-0db51b6d912f",
                   "created_at": "2023-08-09T23:56:06.907067",
                   "updated_at": "2023-08-09T23:56:06.907067",
                   "__class__": "BaseModel"}
        key = f'{my_dict["__class__"]}.{my_dict["id"]}'
        base_obj = BaseModel(**my_dict)
        obj = FileStorage()
        if (not isfile("file.json")):
            objects = obj.all()
            self.assertNotIn(key, list(objects.keys()))
        obj.new(base_obj)
        objects = obj.all()
        self.assertIn(key, list(objects.keys()))

    def test_save(self):
        """ Test the save method """
        obj = FileStorage()
        obj.save()
        self.assertTrue(isfile("file.json"))

    def test_reload(self):
        """ Test the reload method """
        obj = FileStorage()
        obj.reload()
        objects = obj.all()
        if (isfile("file.json")):
            objects = obj.all()
            self.assertTrue(len(objects) > 0)
        else:
            with self.assertRaises(FileNotFoundError):
                with open("file.json", "r") as file:
                    pass
