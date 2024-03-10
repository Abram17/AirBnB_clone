#!/usr/bin/python3
"""
module for the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user class inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
