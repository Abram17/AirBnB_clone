#!/usr/bin/python3
"""
unittests for models/engine/file_storage.py.
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
	"""
	instantiation of FileStorage
	"""

	def test_FileStorage_instantiation_no_args(self):
		self.assertEqual(type(FileStorage()), FileStorage)

	def test_FileStorage_instantiation_with_arg(self):
		with self.assertRaises(TypeError):
			FileStorage(None)

	def test_FileStorage_file_path_is_private_str(self):
		self.assertEqual(str, type(FileStorage.__file_path))

	def testFileStorage_objects_is_private_dict(self):
		self.assertEqual(dict, type(FileStorage.__objects))

	def test_storage_initializes(self):
		self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
	"""
	FileStorage class
	"""

	@classmethod
	def setUp(self):
		try:
			os.rename("file.json", "tmp")
		except IOError:
			pass

	@classmethod
	def tearDown(self):
		try:
			os.remove("file.json")
		except IOError:
			pass
		try:
			os.rename("tmp", "file.json")
		except IOError:
			pass
		FileStorage.__objects = {}

	def test_all(self):
		self.assertEqual(dict, type(models.storage.all()))

	def test_all_arg(self):
		with self.assertRaises(TypeError):
			models.storage.all(None)

	def test_new(self):
		models.storage.new(BaseModel)
		models.storage.new(User)
		models.storage.new(State)
		models.storage.new(Place)
		models.storage.new(City)
		models.storage.new(Amenity)
		models.storage.new(Review)
		self.assertIn("BaseModel." + BaseModel.id, models.storage.all().keys())
		self.assertIn(BaseModel, models.storage.all().values())
		self.assertIn("User." + User.id, models.storage.all().keys())
		self.assertIn(User, models.storage.all().values())
		self.assertIn("State." + State.id, models.storage.all().keys())
		self.assertIn(State, models.storage.all().values())
		self.assertIn("Place." + Place.id, models.storage.all().keys())
		self.assertIn(Place, models.storage.all().values())
		self.assertIn("City." + City.id, models.storage.all().keys())
		self.assertIn(City, models.storage.all().values())
		self.assertIn("Amenity." + Amenity.id, models.storage.all().keys())
		self.assertIn(Amenity, models.storage.all().values())
		self.assertIn("Review." + Review.id, models.storage.all().keys())
		self.assertIn(Review, models.storage.all().values())

	def test_new_args(self):
		with self.assertRaises(TypeError):
			models.storage.new(BaseModel(), 1)

	def test_new_None(self):
		with self.assertRaises(AttributeError):
			models.storage.new(None)

	def test_save(self):
		models.storage.new(BaseModel)
		models.storage.new(User)
		models.storage.new(State)
		models.storage.new(Place)
		models.storage.new(City)
		models.storage.new(Amenity)
		models.storage.new(Review)
		models.storage.save()
		save_text = ""
		with open("file.json", "r") as f:
			save_text = f.read()
			self.assertIn("BaseModel." + BaseModel.id, save_text)
			self.assertIn("User." + User.id, save_text)
			self.assertIn("State." + State.id, save_text)
			self.assertIn("Place." + Place.id, save_text)
			self.assertIn("City." + City.id, save_text)
			self.assertIn("Amenity." + Amenity.id, save_text)
			self.assertIn("Review." + Review.id, save_text)

	def test_save_arg(self):
		with self.assertRaises(TypeError):
			models.storage.save(None)

	def test_reload(self):
		models.storage.new(BaseModel)
		models.storage.new(User)
		models.storage.new(State)
		models.storage.new(Place)
		models.storage.new(City)
		models.storage.new(Amenity)
		models.storage.new(Review)
		models.storage.save()
		models.storage.reload()
		objs = FileStorage.__objects
		self.assertIn("BaseModel." + BaseModel.id, objs)
		self.assertIn("User." + User.id, objs)
		self.assertIn("State." + State.id, objs)
		self.assertIn("Place." + Place.id, objs)
		self.assertIn("City." + City.id, objs)
		self.assertIn("Amenity." + Amenity.id, objs)
		self.assertIn("Review." + Review.id, objs)

	def test_reload_arg(self):
		with self.assertRaises(TypeError):
			models.storage.reload(None)


if __name__ == "__main__":
	unittest.main()
