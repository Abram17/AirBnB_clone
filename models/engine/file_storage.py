#!/usr/bin/python3
"""
contains the FileStorage class
"""

import json
import os
from models.base_model import BaseModel

class FileStorage:
	"""
	serializes instances to a JSON file and deserializes JSON file to instances
	"""

	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""
		 returns the dictionary __objects
		"""
		return FileStorage.__objects

	def new(self, obj):
		"""
		sets in __objects the obj with key <obj class name>.id
		"""
		key = "{}.{}".format(obj.__class__.__name__, obj.id)
		FileStorage.__objects[key] = obj

	def save(self):
		"""
		serializes __objects to the JSON file (path: __file_path)
		"""
		with open(FileStorage.__file_path, "w", encoding = "utf-8") as file:
			j = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
			json.dump(j, file)

	def reload(self):
		"""
		deserializes the JSON file to __objects
		"""
		if os.path.isfile(FileStorage.__file_path):
			with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
				obj_dict = json.load(file)
				try:
					obj_dict = {key: self.classes()[value["__class__"]](**value)\
					for key, value in obj_dict.items()}
					FileStorage.__objects = obj_dict
				except Exception:
					pass

	def existing(self):
		"""
		valid classes for the cmd
		"""

		from models.base_model import BaseModel
		from models.user import User
		from models.city import City
		from models.amenity import Amenity
		from models.state import State
		from models.place import Place
		from models.review import Review

		existing = {
			"BaseModel" : BaseModel,
			"User" : User,
			"City" : City,
			"State" : State,
			"Place" : Place,
			"Amenity" : Amenity,
			"Review" : Review
		}

		return existing
