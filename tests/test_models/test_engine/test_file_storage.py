#!/usr/bin/python3
"""Testin' file_storage"""
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """class for testing basic cases
    on FileStorage"""

    def test_all(self):
        """Test that it returns well
        all dictionary __objects"""
        store = FileStorage()
        dic_obj = store.all()
        self.assertDictEqual(dic_obj, {})
        self.assertEqual(type(dic_obj), dict)

    def test_save(self):
        """Test the save function"""
        self.setUp()
        self.assertEqual(os.path.getsize("file.json"), 2)
        os.remove("file.json")
        model = BaseModel()
        model.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertGreater(os.path.getsize("file.json"), 2)
    
    def test_reload(self):
        """Testing if object is recreated from json"""
        FileStorage._FileStorage__objects = {}
        FileStorage().save()
        base = BaseModel()
        FileStorage().save()
        FileStorage._FileStorage__objects = {}
        self.assertEqual(len(FileStorage().all()), 0)
        FileStorage().reload()
        self.assertEqual(len(FileStorage().all()), 2)

if __name__ == "__main__":
    unittest.main()
