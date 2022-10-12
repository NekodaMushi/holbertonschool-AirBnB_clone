#!/usr/bin/python3
"""Testing State"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """State Testing"""
    
    def test_var_validity(self):
        """Method testing State Variables"""
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertEqual(s.name, "")

if __name__ == '__main__':
    unittest.main()
