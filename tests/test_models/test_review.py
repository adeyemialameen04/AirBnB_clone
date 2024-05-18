#!/usr/bin/python3
"""Documenting module."""
import unittest
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Docs for test state"""
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage.__FileStorage__object = {}

    def test_pub_attrs(self):
        review = Review()
        review.place_id = "Lagos"
        review.text = "Random text"
        review.user_id = "mugiwara"
        self.assertIsNotNone(review.updated_at)
        self.assertIsNotNone(review.updated_at)
        self.assertIsNotNone(review.id)
        self.assertEqual(review.place_id, "Lagos")
        self.assertEqual(review.user_id, "mugiwara")
        self.assertEqual(review.text, "Random text")


if __name__ == "__main__":
    unittest.main()
