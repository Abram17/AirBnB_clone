#!/usr/bin/python3
"""
module that contains the review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from the base model
    """
    place_id = ""
    user_id = ""
    text = ""
