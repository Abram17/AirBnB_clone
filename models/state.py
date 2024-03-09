#!/usr/bin/python3
"""
module that contains the State class
"""
from models.base_model import BaseModel

class State(BaseModel):
	"""
	state class that inherits from the BaseModel
	"""
	name = ""

	def __init__(self, *args, **kwargs):
		"""
		initilizes the State class
		"""
		super().__init__(*args, **kwargs)
