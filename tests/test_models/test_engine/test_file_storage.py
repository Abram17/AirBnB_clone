#!/usr/bin/python3
"""
tests for FileStorage class
"""
import models
import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorageInst(unittest.TestCase):
    """
    test file storage instantiation
    """
    def test_FileStorage_instantiation(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    """
    Tests the FileStorage class
    """
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        new_model = BaseModel()
        new_user = User()
        new_amenity = Amenity()
        new_city = City()
        new_place = Place()
        new_review = Review()
        new_state = State()
        models.storage.new(new_model)
        models.storage.new(new_user)
        models.storage.new(new_amenity)
        models.storage.new(new_place)
        models.storage.new(new_city)
        models.storage.new(new_review)
        models.storage.new(new_state)
        self.assertIn("BaseModel." + new_model.id, models.storage.all().keys())
        self.assertIn(new_model, models.storage.all().values())
        self.assertIn("User." + new_user.id, models.storage.all().keys())
        self.assertIn(new_user, models.storage.all().values())
        self.assertIn("State." + new_state.id, models.storage.all().keys())
        self.assertIn(new_state, models.storage.all().values())
        self.assertIn("City." + new_city.id, models.storage.all().keys())
        self.assertIn(new_city, models.storage.all().values())
        self.assertIn("Amenity." + new_amenity.id, models.storage.all().keys())
        self.assertIn(new_amenity, models.storage.all().values())
        self.assertIn("Place." + new_place.id, models.storage.all().keys())
        self.assertIn(new_place, models.storage.all().values())
        self.assertIn("Review." + new_review.id, models.storage.all().keys())
        self.assertIn(new_review, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        new_model = BaseModel()
        new_user = User()
        new_amenity = Amenity()
        new_city = City()
        new_place = Place()
        new_review = Review()
        new_state = State()
        models.storage.new(new_model)
        models.storage.new(new_user)
        models.storage.new(new_amenity)
        models.storage.new(new_place)
        models.storage.new(new_city)
        models.storage.new(new_review)
        models.storage.new(new_state)
        models.storage.save()
        saved = ""
        with open("file.json", "r") as f:
            saved = f.read()
            self.assertIn("BaseModel." + new_model.id, saved)
            self.assertIn("User." + new_user.id, saved)
            self.assertIn("State." + new_state.id, saved)
            self.assertIn("Place." + new_place.id, saved)
            self.assertIn("City." + new_city.id, saved)
            self.assertIn("Amenity." + new_amenity.id, saved)
            self.assertIn("Review." + new_review.id, saved)

    def test_save_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        new_model = BaseModel()
        new_user = User()
        new_amenity = Amenity()
        new_city = City()
        new_place = Place()
        new_review = Review()
        new_state = State()
        models.storage.new(new_model)
        models.storage.new(new_user)
        models.storage.new(new_amenity)
        models.storage.new(new_place)
        models.storage.new(new_city)
        models.storage.new(new_review)
        models.storage.new(new_state)
        o = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + new_model.id, o)
        self.assertIn("User." + new_user.id, o)
        self.assertIn("Place." + new_place.id, o)
        self.assertIn("Amenity." + new_amenity.id, o)
        self.assertIn("State." + new_state.id, o)
        self.assertIn("City." + new_city.id, o)
        self.assertIn("Review." + new_review.id, o)

    def test_reload_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
