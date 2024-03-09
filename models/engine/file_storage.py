#!/usr/bin/python3
""" module for file storage functionality using JSON """
import json


class FileStorage:
    """ that serializes instances to a JSON
        file and deserializes JSON file to instances

        Attributes:
            __file_path:        path to the file to write data on
            __objects:          dict of objects to serialize
        Methods:
            all(self):          returns contents of the __objects dictionary.
            new(self, obj):     adds objects to __objects dict with
                                '<class name>.id' as their key.
            save(self):         writes __objects dictionary into a json file.
            reload(self):       reads the json file and writes its data into
                                the __objects dictionary.
    """
    
    __file_path = 'file.json'
    __objects = {}

    @property
    def testobjects(self):
        """ property getter for testing purposes """
        return self.__objects
    
    @property
    def testfilepath(self):
        """property setter for testing purposes """
        return self.__file_path
    
    @testobjects.setter
    def testobjects(self, objects_dict):
        """ property getter for testing purposes """
        self.__objects = objects_dict

    @testfilepath.setter
    def testfilepath(self, path):
        """property setter for testing purposes """
        self.__file_path = path

    def all(self):
        """ retuns the dict __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[f"{obj['__class__']}.{obj['id']}"] = obj

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except:
            return
