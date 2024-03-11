#!/usr/bin/python3
"""
tests for FileStorage class
"""
import models
import os
import unittest
from models.base_model import BaseModel
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
        models.storage.new(new_model)
        self.assertIn("BaseModel." + new_model.id, models.storage.all().keys())
        self.assertIn(new_model, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        new_model = BaseModel()
        models.storage.new(new_model)
        models.storage.save()
        saved = ""
        with open("file.json", "r") as f:
            saved = f.read()
            self.assertIn("BaseModel." + new_model.id, saved)

    def test_save_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        new_model = BaseModel()
        models.storage.new(new_model)
        o = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + new_model.id, o)

    def test_reload_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
