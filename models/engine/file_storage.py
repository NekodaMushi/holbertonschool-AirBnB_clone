#!/usr/bin/python3
"""Function giving the possibility to stores and 
restores any objects created before"""
import json
from models.base_model import BaseModel

class FileStorage:
    """Storage class"""

    def __init__(self):
        """Init: FileStorage
       Var:
       """
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """Returns dictionnary __objects"""
        return self.__objects

    def new(self,obj):
        """sets in __objects the obj 
        with key <obj class name>.id"""
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}":obj})

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
                    #Use eval because you wanna reconstruct an object
                    self.__objects[key] = eval(value['__class__'])(**value)
        #Get all exceptions possible
        except Exception:
            pass
