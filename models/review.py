#!/usr/bin/python3
"""
Defines a module for the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents an instance of a review
    """

    place_id = ""
    user_id = ""
    text = ""
