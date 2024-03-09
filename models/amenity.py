#!/usr/bin/python3
"""
Module that contains the Amenity class
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
	"""
	Amenity class that inherits from the BaseModel
	"""
	name = ""

	def __init__(self, *args, **kwargs):
		"""
		initilizes the amenity class
		"""
		super().__init__(*args, **kwargs)
