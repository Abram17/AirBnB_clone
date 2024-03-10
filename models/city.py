#!/usr/bin/python3
"""
module that contains the City model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    city class that inherits from the BaseModel
    """
    state_id = ""
    name = ""
