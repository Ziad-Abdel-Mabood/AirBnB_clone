#!/usr/bin/python3
""" test unit for base_model.py """
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """ Testing the BaseModel Class functionality
        which will pass on common attributes to all
        other classes/models
    """

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_initialization(self):
        """ testing basic functionality"""
        with self.subTest('Exists & correct type'):
            self.assertTrue(isinstance(self.my_model, BaseModel))
            self.assertTrue(isinstance(self.my_model.id, str))
        
        with self.subTest('Can add attributes'): 
            self.assertTrue(isinstance(self.my_model.name, str))
            self.assertTrue(isinstance(self.my_model.my_number, int))

    def test_updating(self):
        """ testing the save() method """
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_dict(self):
        """ testing to_dict() method that returns
            dict representation of the object
        """
        self.my_model_dict = self.my_model.to_dict()
        self.assertTrue('id' in self.my_model_dict)
        self.assertTrue('__class__' in self.my_model_dict)
        self.assertTrue('created_at' in self.my_model_dict)
        self.assertTrue('updated_at' in self.my_model_dict)
        self.assertTrue('name' in self.my_model_dict)
        self.assertTrue('my_number' in self.my_model_dict)

if __name__ == '__main__':
    unittest.main()
