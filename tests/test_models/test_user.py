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
        user.email = "adeyemialameen04@gmail.com"
        self.assertIsNotNone(user.updated_at)
        self.assertIsNotNone(user.id)
        self.assertEqual(user.first_name, "Al-ameen")
        self.assertEqual(user.last_name, "Adeyemi")
        self.assertEqual(user.email, "adeyemialameen04@gmail.com")


if __name__ == "__main__":
    unittest.main()
