#!/usr/bin/python3
"""Documenting module."""
import unittest
from models.place import Place
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """Docs for test place"""
    def setUp(self):
        """Setup."""
        self.storage = FileStorage()

    def tearDown(self):
        """Teardown."""
        self.storage.__FileStorage__object = {}

    def test_pub_attrs(self):
        """Tests the attrs."""
        place = Place()
        place.city_id = "Lagos"
        place.user_id = "mugiwara"
        place.name = "Onipanu"
        place.description = "Before palmgroove"
        place.number_rooms = 20
        place.number_bathrooms = 10
        place.max_guest = 5
        place.price_by_night = 500
        place.longitude = 20.9
        place.latitude = 90.8
        self.assertIsNotNone(place.updated_at)
        self.assertIsNotNone(place.updated_at)
        self.assertIsNotNone(place.id)
        self.assertEqual(place.user_id, "mugiwara")
        self.assertEqual(place.city_id, "Lagos")
        self.assertEqual(place.name, "Onipanu")
        self.assertEqual(place.description, "Before palmgroove")
        self.assertEqual(place.number_rooms, 20)
        self.assertEqual(place.number_bathrooms, 10)
        self.assertEqual(place.max_guest, 5)
        self.assertEqual(place.price_by_night, 500)
        self.assertEqual(place.longitude, 20.9)
        self.assertEqual(place.latitude, 90.8)


if __name__ == "__main__":
    unittest.main()
