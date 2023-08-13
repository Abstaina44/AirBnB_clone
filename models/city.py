#!/usr/bin/python3
"""
Defines a module for the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents an instance of a city
    """

    state_id = ""
    name = ""
