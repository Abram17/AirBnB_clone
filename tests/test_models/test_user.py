#!/usr/bin/python3
"""
tests for the user class
"""
import models
import os
import unittest
from datetime import datetime
from time import sleep
from models.user import User

class TestUserInst(unittest.TestCase):
    """
    tests the user class instantation
    """

    def test_user_inst(self):
        self.assertEqual(User, type(User()))

    def test_new_inst(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email(self):
        self.assertEqual(str, type(User.email))

    def test_password(self):
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        self.assertEqual(str, type(User.last_name))

    def test_different_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_at(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_kwargs(self):
        us = User(id = "777",
                  created_at = datetime.utcnow().isoformat(),
                  updated_at = datetime.utcnow().isoformat())
        self.assertEqual(us.id, "777")
        self.assertEqual(us.created_at, datetime.utcnow())
        self.assertEqual(us.updated_at, datetime.utcnow())

    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_args(self):
        self.assertNotIn(None, User(None).__dict__.values())

    def test_str(self):
        new_user = User()
        new_user.id = "777"
        new_user.created_at = new_user.updated_at = datetime.utcnow()
        self.assertIn("[User] (777)", new_user.__str__)
        self.assertIn("'id': '777'", new_user.__str__)
        self.assertIn("'created_at: '" + repr(datetime.utcnow()), new_user.__str__)
        self.assertIn("'updated_at: '" + repr(datetime.utcnow()), new_user.__str__)
