#!/usr/bin/python3
"""
contains unittests for the BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        new_model = BaseModel()
        self.assertIsNotNone(new_model.id)
        self.assertIsNotNone(new_model.created_at)
        self.assertIsNotNone(new_model.updated_at)

    def test_save(self):
        new_model = BaseModel()
        first = new_model.updated_at
        second = new_model.save()
        self.assertNotEqual(first, second)

    def test_to_dict(self):
        new_model = BaseModel()
        new_model_d = new_model.to_dict()
        self.assertIsInstance(new_model_d, dict)
        self.assertEqual(new_model_d["__class__"], "BaseModel")
        self.assertEqual(new_model_d["id"], new_model.id)
        self.assertEqual(new_model_d["created_at"], new_model.created_at.isoformat())
        self.assertEqual(new_model_d["updated_at"], new_model.updated_at.isoformat())

    def test_str(self):
        new_model = BaseModel()
        self.assertTrue(str(new_model).startswith("[BaseModel]"))
        self.assertIn(new_model.id, str(new_model))
        self.assertIn(str(new_model.__dict__), str(new_model))


if __name__ == "__main__":
    unittest.main()
