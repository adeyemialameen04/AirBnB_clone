#!/usr/bin/python3
"""Documenting module."""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    def test_prompt(self):
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")


if __name__ == "__main__":
    unittest.main()
