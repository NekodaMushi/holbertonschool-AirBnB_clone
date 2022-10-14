#!/usr/bin/python3
"""Unittest User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing User Class"""

    def test_var_validity(self):
        """Testing differents parameters of User"""
        u0 = User()
        self.assertTrue(hasattr(u0, "email"))
        self.assertTrue(hasattr(u0, "password"))
        self.assertTrue(hasattr(u0, "first_name"))
        self.assertTrue(hasattr(u0, 'last_name'))
        self.assertEqual(u0.email, "")
        self.assertEqual(u0.password, "")
        self.assertEqual(u0.first_name, "")
        self.assertEqual(u0.last_name, "")


if __name__ == '__main__':
    unittest.main()
