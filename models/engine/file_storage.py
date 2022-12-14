#!/usr/bin/python3
"""Function giving the possibility to stores and
restores any objects created before"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Storage class
    Private class attributes:
    __file_path === Path to JSON File
    __objects === dictionary to store all objects
    by <classname>.id
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionnary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj
        with key <obj class name>.id"""
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """Serializes __objects to the JSON file"""
        serial_dict = {}
        for key in self.__objects.keys():
            serial_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w+") as write_file:
            json.dump(serial_dict, write_file)

    def reload(self):
        """deserializes the JSON file to
        __objects (only if the JSON file"""
        try:
            with open(self.__file_path, "r+") as data:
                JSONdata = json.load(data)
                for key, value in JSONdata.items():
                    # Use eval because you wanna reconstruct an instance
                    self.__objects[key] = eval(value['__class__'])(**value)
        # Get all exceptions possible
        except Exception:
            pass
