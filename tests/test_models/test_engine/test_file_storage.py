#!/usr/bin/python3
"""Documenting module."""
import os
import unittest
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Documenting for FileStorage"""

    def setUp(self):
        """Setup"""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        self.objects = self.storage._FileStorage__objects

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_new(self):
        inst = User()
        self.storage.new(inst)
        key = f"{inst.__class__.__name__}.{inst.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        inst = User()
        self.storage.new(inst)
        self.storage.save()
        self.assertEqual(self.file_path, self.storage._FileStorage__file_path)
        self.assertTrue(os.path.exists(self.file_path))
        # Unfinished

    def test_all(self):
        inst_1, inst_2 = User(), User()
        self.storage.new(inst_1)
        self.storage.new(inst_2)
        self.storage.save()
        key_1, key_2 = (f"{inst_1.__class__.__name__}.{inst_1.id}",
                        f"{inst_2.__class__.__name__}.{inst_2.id}")
        self.assertIn(key_1, self.storage.all())
        self.assertIn(key_2, self.storage.all())
        self.assertGreaterEqual(len(self.storage.all()), 2)

    def test_reload(self):
        inst = User()
        self.storage.new(inst)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"{inst.__class__.__name__}.{inst.id}"
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
