#!/usr/bin/python3
"""
Defines a module for the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents an instance of a user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
