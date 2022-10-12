#!/usr/bin/python3
"""Testing Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Civility Testing"""
    
    def test_var_validity(self):
        """Method testing Amenity Variables"""
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "")
