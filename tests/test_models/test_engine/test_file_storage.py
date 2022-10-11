#!/usr/bin/python3
"""Testin' file_storage"""
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """class for testing basic cases
    on FileStorage"""

    def test_all(self):
        """Test that it returns well
        all dictionary __objects"""
        store = FileStorage()
        dic_obj = store.all()
        self.assertIsNotNone(dic_obj)
        self.assertEqual(type(dic_obj), dict)
