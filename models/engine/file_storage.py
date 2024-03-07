#!/usr/bin/python3
""" module for file storage functionality using JSON """
import json


class FileStorage:
    """ that serializes instances to a JSON
        file and deserializes JSON file to instances

        Attributes:
            __file_path:     path to the file to write data on
            __objects:      dict of objects to serialize
    """
    
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ retuns the dict __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[f"{obj['__class__']}.{obj['id']}"] = obj

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path) """
        f = open(self.__file_path, 'w')
        json.dump(self.__objects, f)
        f.close()

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            f = open(self.__file_path, 'r')
            self.__objects = json.load(f)
            f.close()
        except:
            return
