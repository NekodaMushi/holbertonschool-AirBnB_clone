#!/usr/bin/python3
"""Review Test"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Review Test Class"""

    def test_var_validity(self):
        """Method testing variables
        validity in class Review"""
        r = Review()
        self.assertTrue(hasattr(r, "place_id"), True)
        self.assertTrue(hasattr(r, "user_id"), True)
        self.assertFalse(hasattr(r, "test"), False)
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")
