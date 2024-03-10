#!/usr/bin/python3
"""
contains the BaseModel class
"""

from datetime import datetime
from uuid import uuid4
from models import storage

class BaseModel:
	"""
	defines all common attributes/methods for other classes
	"""

	def __init__(self, *args, **kwargs):
		"""
		initilizes BaseModel
		"""

		time = "%Y-%m-%dT%H:%M:%S.%f"

		if kwargs is None and kwargs == {}:
			self.id = str(uuid4)
			self.created_at = datetime.utcnow()
			self.updated_at = datetime.utcnow()
			storage.new(self)

		else:
			for key, value in kwargs.items():
				if key == "__class__":
					continue
				elif key == "updated_at" | key == "created_at":
					setattr(self, key, datetime.strptime(value, time))
				else:
					setattr(self, key, value)

	def save(self):
		"""
		updates the public instance attribute updated_at with the current datetime
		"""
		storage.save()
		self.updated_at = datetime.utcnow()

	def to_dict(self):
		"""
		returns a dictionary containing all keys/values of __dict__ of the instance
		"""

		this_dict = self.__dict__.copy()
		this_dict["__class__"] = self.__class__.__name__
		this_dict["created_at"] = self.created_at.isoformat()
		this_dict["updated_at"] = self.updated_at.isoformat()

		return this_dict

	def __str__(self):
		"""
		print: [<class name>] (<self.id>) <self.__dict__>
		"""

		return "[{}] ({}) {}"\
			.format(self.__class__.__name__, self.id, self.__dict__)
