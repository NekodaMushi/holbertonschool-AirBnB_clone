#!/usr/bin/python3
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class for testing to gik"""

    def test_save(self):
        """test saving function"""
        b = BaseModel(5, 2, 6)
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_dict(self):
        """test to_dict function"""
        b = BaseModel()
        b.name = "Fabien"
        b.age = "57"
        b.country = "Australia"
        dic = b.to_dict()
        self.assertEqual(dic["name"], b.name)
        self.assertEqual(dic["age"], b.age)
        self.assertEqual(dic["country"], b.country)

    def test_str(self):
        """testing the string representation"""
        b = BaseModel()
        checker = f"[{(b).__class__.__name__}] ({b.id}) {b.__dict__}"
        self.assertEqual(str(b), checker)
