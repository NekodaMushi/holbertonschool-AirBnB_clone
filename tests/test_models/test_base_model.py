#!/usr/bin/python3
"""Unittest"""
import unittest
from datetime import datetime
from unittest.mock import Base
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """BaseModel Test Class"""
    def testId(self):
        b0= BaseModel()
        b0.number = 32
        b0.string = "Chung"
        b0.fail = None
        b0.save()
        self.assertNotEqual(b0.created_at, b0.updated_at)

    def test__str__(self):
        b1 = BaseModel()
        checker = [f"[{(b1).__name__}] ({b1.id}) {b1.__dict__}"]
        self.assertEqual(str(b1), checker)

if __name__ == '__main__':
    unittest.main()
