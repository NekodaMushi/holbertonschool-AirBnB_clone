#!/usr/bin/python3
"""Unittest"""
import unittest
from datetime import datetime
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

    def test_save(self):
        """Testing if save by checking different before and after checker"""
        bs = BaseModel()
        bef_created_at = bs.created_at
        bef_updated_at = bs.updated_at
        bs.save()
        aft_created_at = bs.created_at
        aft_updated_at = bs.updated_at
        self.assertEqual(bef_created_at, aft_created_at)
        self.assertNotEqual(bef_updated_at, aft_updated_at)
        self.assertNotEqual(aft_created_at, aft_updated_at)



if __name__ == '__main__':
    unittest.main()
