import json
from os import path
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj): # Sets in __objects [key <obj class name>.id] = obj
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def reload(self): # Deserializes the JSON file to __objects
        """Deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    loaded_objects = json.load(f)
                    for key, obj_dict in loaded_objects.items():
                        class_name, obj_id = key.split('.')
                        obj_class = globals()[class_name]
                        self.__objects[key] = obj_class(**obj_dict)
                except json.JSONDecodeError:
                    pass 

    def all(self): # Return self.__object [key <obj class name>.id] = obj
        """Returns the dictionary __objects"""
        return self.__objects
    
    def save(self): # To json file [key <obj class name>.id] = obj.to_dict()
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)