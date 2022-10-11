#!/usr/bin/python3
"""Unittest"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """BaseModel Test Class"""
    def testSave(self):
        b0= BaseModel()
        b0.number = 32
        b0.string = "Chung"
        b0.fail = None
        b0.save()
        self.assertNotEqual(b0.created_at, b0.updated_at)
