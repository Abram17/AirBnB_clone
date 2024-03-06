#!/usr/bin/python3
"""
"""
import unittest
from models.base_model import BaseModel

class TBaseModel(unittest.TestCase):
	def test_init(self):
		model = BaseModel()

		self.assertIsNotNone(model.id)
		self.assertIsNotNone(model.created_at)
		self.assertIsNotNone(model.updated_at)

	def test_save(self):
		model = BaseModel()
		first_updated = model.updated_at
		second_updated = model.save()

		self.assertNotEqual(first_updated, second_updated)

	def test_to_dict(self):
		model = BaseModel()
		model_dict = model.to_dict()

		self.assertIsInstance(model_dict, dict)
		self.assertEqual(model_dict["__class__"], 'BaseModel')
		self.assertEqual(model_dict["id"], model.id)
		self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
		self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())

	def test_str(self):
		model = BaseModel()

		self.assertTrue(str(model).startswith('[BaseModel]'))
		self.assertIn(model.id, str(model))
		self.assertIn(str(model.__dict__), str(model))

	if __name__ == "__main__":
		unittest.main()
