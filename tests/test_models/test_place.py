#!/usr/bin/python3
"""Unittest Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Place Test Class"""

    def test_var_validity(self):
        """Method testing validity
        of variable in Place"""
        p = Place()
        self.assertTrue(p, "city_id")
        self.assertTrue(p, "user_id")
        self.assertTrue(p, "name")
        self.assertTrue(p, "description")
        self.assertTrue(p, "number_rooms")
        self.assertTrue(p, "number_bathrooms")
        self.assertTrue(p, "max_guest")
        self.assertTrue(p, "price_by_night")
        self.assertTrue(p, "latitude")
        self.assertTrue(p, "longitude")
        self.assertTrue(p, "amenity")
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, "")
        self.assertEqual(p.number_bathrooms, "")
        self.assertEqual(p.max_guest, "")
        self.assertEqual(p.price_by_night, "")
        self.assertEqual(p.latitude, "")
        self.assertEqual(p.amenity_ids, "")


if __name__ == '__main__':
    unittest.main()
