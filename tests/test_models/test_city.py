#!/usr/bin/python3
"""Unitest City"""
import imp
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Testing City Class"""

    def test_var_validity(self):
        """Testing differents parameters of City"""
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "name"))
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")


if __name__ == '__main__':
    unittest.main()
