#!/usr/bin/python3
"""Documenting module."""
import unittest
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """Docs for test city"""
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage.__FileStorage__object = {}

    def test_pub_attrs(self):
        city = City()
        city.name = "Lagos"
        city.state_id = "Lagos"
        self.assertIsNone(city.created_at)
        self.assertIsNotNone(city.id)
        self.assertEqual(city.name, "Lagos")
        self.assertEqual(city.state_id, "Lagos")


if __name__ == "__main__":
    unittest.main()
