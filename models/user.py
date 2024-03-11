#!/usr/bin/python3
"""
module that contains the user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
