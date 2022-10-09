#!/usr/bin/python3
"""Base defining all common attributes/methods for other classes:"""
from datetime import datetime
import uuid


class BaseModel:
    """Mother Class of all within this project"""

    def __init__(self, *args, **kwargs):
        """Init: BaseModel
        Args: Key
        Kwargs: Value"""

        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())


        for key, mydate in kwargs.items():
            if key == "created_at" or key == "updated_at":
                mydate = datetime.strptime(mydate, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, mydate)
            else:
                setattr(self, key, mydate)

    def __str__(self):
        """String Representation of Object"""

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance attribute
        with current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary 
        containing all keys/values of 
        __dict__ of the instance"""

        dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dict[key] = value
        dict["__class__"] = self.__class__.__name__
        return dict
