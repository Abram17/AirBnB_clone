#!/usr/bin/python3
"""
tests for the amenity class
"""
import models
import os
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

class TestAmenityInst(unittest.TestCase):
    """
    tests the Amenity class instantation
    """

    def test_ameniy_inst(self):
        self.assertEqual(Amenity(), type(Amenity()))

    def test_new_inst(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_different_ids(self):
        user1 = Amenity()
        user2 = Amenity()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_at(self):
        user1 = Amenity()
        sleep(0.1)
        user2 = Amenity()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        user1 = Amenity()
        sleep(0.1)
        user2 = Amenity()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_kwargs(self):
        us = Amenity(id = "777",
                  created_at = datetime.utcnow().isoformat(),
                  updated_at = datetime.utcnow().isoformat())
        self.assertEqual(us.id, "777")
        self.assertEqual(us.created_at, datetime.utcnow())
        self.assertEqual(us.updated_at, datetime.utcnow())

    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_args(self):
        self.assertNotIn(None, Amenity(None).__dict__.values())

    def test_str(self):
        new_user = Amenity()
        new_user.id = "777"
        new_user.created_at = new_user.updated_at = datetime.utcnow()
        self.assertIn("[Amenity] (777)", new_user.__str__)
        self.assertIn("'id': '777'", new_user.__str__)
        self.assertIn("'created_at: '" + repr(datetime.utcnow()), new_user.__str__)
        self.assertIn("'updated_at: '" + repr(datetime.utcnow()), new_user.__str__)
