#!/usr/bin/python3
"""Unittest"""
import unittest
from datetime import datetime
from unittest.mock import Base
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """BaseModel Test Class"""

    def testId(self):
        b0 = BaseModel()
        b0.number = 32
        b0.string = "Chung"
        b0.fail = None
        b0.save()
        self.assertNotEqual(b0.created_at, b0.updated_at)

    def test__str__(self):
        b1 = BaseModel()
        checker = (f"[{b1.__class__.__name__}] ({b1.id}) {b1.__dict__}")
        self.assertEqual(str(b1), checker)

    def test_todict(self):
        """test a dict"""
        model = BaseModel()
        model.name = "Odin"
        model.price = 2
        model.note = "really good"
        d = model.to_dict()
        exp_attrib = ["id",
                      "created_at",
                      "updated_at",
                      "name",
                      "price",
                      "really good",
                      "__class__"]
        self.assertEqual(d["name"], "Odin")
        self.assertEqual(d["price"], 2)
        self.assertEqual(d["note"], "really good")
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(len(d.keys()), len(exp_attrib))


if __name__ == '__main__':
    unittest.main()
