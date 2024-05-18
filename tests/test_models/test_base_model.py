#!/usr/bin/python3
"""Documenting the user model"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """The test class for basemodel."""

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage.__FileStorage__object = {}

    def test_pub_attrs(self):
        model = BaseModel()
        model.name = "My model"
        model.number = 15
        self.assertEqual(model.name, "My model")
        self.assertEqual(model.number, 15)

    def test_datetime(self):
        """tests for datetime"""
        pass

    def test_datetime(self):
        """tests for datetime"""
        pass


if __name__ == "__main__":
    unittest.main()
