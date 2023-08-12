#!/usr/bin/python3
"""
This module defines the generic attributes and
behaviours for other classes.
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Defines the BaseModel class. The parent class
    with common members for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the BaseModel.

        Parameters
        args : tuple
            A non-keyworded variable number of
            arguments.
        kwargs : dictionary
            A key-worded variable number of
            arguments.
        """
        if (kwargs == {}):
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if (key == "__class__"):
                    continue
                setattr(self, key, datetime.fromisoformat(value)
                        if ("_at" in key) else value)

    def __str__(self):
        """
        Returns a string representation for
        an instance.
        """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates the `updated_at` attribute
        with the current date time.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary of attributes
        belonging toan instance.
        """
        obj_dict = {}

        for key, value in self.__dict__.items():
            obj_dict[key] = value.isoformat() if ("_at" in key) else value
        obj_dict["__class__"] = type(self).__name__

        return (obj_dict)
