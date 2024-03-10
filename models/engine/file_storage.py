#!/usr/bin/python3
"""
contains the FileStorage class
"""

import json
import os
from datetime import datetime
import models

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
		object_dict = {}

		for key in self.__objects.keys():
			if type(self.__objects[key]) != dict:
				object_dict[key] = self.__objects[key].to_dict()
		file_name = self.__file_path
		with open(file_name, "w", encoding="utf-8") as jsonfile:
			jsonfile.write(json.dumps(object_dict))

	def reload(self):
		"""
		Reloads the stored objects
		"""
		if os.path.exists(FileStorage.__file_path):
			with open(FileStorage.__file_path, "r", encoding="utf-8") \
					as my_file:
				obj_dict = json.loads(my_file.read())
			final_dict = {}

			for id, dictionary in obj_dict.items():
				class_name = dictionary['__class__']
				final_dict[id] = self.existing()[class_name](**dictionary)
			FileStorage.__objects = final_dict

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

	def attributes(self):
		"""
		Contains the valid attributes
		"""
		attributes = {
			"BaseModel":
				{"id": str,
				"created_at": datetime,
				"updated_at": datetime},
			"User":
				{"email": str,
				"password": str,
				"first_name": str,
				"last_name": str},
			"State":
				{"name": str},
			"City":
				{"state_id": str,
				"name": str},
			"Amenity":
				{"name": str},
			"Place":
				{"city_id": str,
				"user_id": str,
				"name": str,
				"description": str,
				"number_rooms": int,
				"number_bathrooms": int,
				"max_guest": int,
				"price_by_night": int,
				"latitude": float,
				"longitude": float,
				"amenity_ids": list},
			"Review":
				{"place_id": str,
				"user_id": str,
				"text": str}
		}
		return attributes
