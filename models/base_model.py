#!/usr/bin/python3
"""
AirBnB project
"""

import models
from datetime import datetime
from uuid import uuid4

class BaseModel:
	"""
	defines all common attributes/methods for other classes
	"""
	def __init__(self):
		"""
		"""
		self.id = str(uuid4)
		self.created_at = datetime.utcnow()
		self.updated_at = datetime.utcnow()

	def save(self):
		"""
		updates the public instance attribute updated_at with the current datetime
		"""

		self.updated_at = datetime.utcnow()

	def to_dict(self):
		"""
		returns a dictionary containing all keys/values of __dict__ of the instanc
		"""
		i_dict = self.__dict__.copy()
		i_dict["__class__"] = self.__class__.__name__
		i_dict["created_at"] = self.created_at.isoformat()
		i_dict["updated_at"] = self.updated_at.isoformat()

		return i_dict

	def __str__(self):
		"""
		return the required format
		"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
