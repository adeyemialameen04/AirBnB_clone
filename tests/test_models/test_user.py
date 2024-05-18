#!/usr/bin/python3
"""Documenting module."""
import unittest
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Docs for test user"""
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage.__FileStorage__object = {}

    def test_pub_attrs(self):
        user = User()
        user.last_name = "Adeyemi"
        user.first_name = "Al-ameen"
        user.password = "Yare"
        user.email = "adeyemialameen04@gmail.com"
        self.assertIsNone(user.created_at)
        self.assertIsNotNone(user.id)
        self.assertEqual(user.first_name, "Al-ameen")
        self.assertEqual(user.last_name, "Adeyemi")
        self.assertEqual(user.email, "adeyemialameen04@gmail.com")
        self.assertEqual(user.password, "Yare")


if __name__ == "__main__":
    unittest.main()
