#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the object dictionaries"""
        if cls is None:
            return self.__objects
        
        cls_dict = {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return cls_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        k = f"{obj.__class__.__name__}+'.'+ {obj.id}"
        self.__objects[k] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(temp, f)

    def delete(self, obj=None):
        """ deletes object from __objects if it is in __objects"""
        if obj is None:
            return
        if obj:
            k = f"{obj.__class__.__name__}+'.'+ {obj.id}"
        if k in self.__objects:
            del self.__objects[k]

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            self.__objects = {}
        except json.JSONDecodeError:
            self.__objects = {}

    def close(self):
        self.reload()