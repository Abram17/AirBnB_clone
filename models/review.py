#!/usr/bin/python3
"""
This module that contains the Review class
"""
from models.base_model import BaseModel

class Review(BaseModel):
	"""
	review class that inherits from the BaseModel
	"""
	place_id = ""
	user_id = ""
	text = ""
