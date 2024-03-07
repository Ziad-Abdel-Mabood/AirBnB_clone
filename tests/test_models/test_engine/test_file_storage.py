#!/usr/bin/python3
""" unittest for file_storage.py """
from models.engine.file_storage import  FileStorage
from models.base_model import BaseModel
from models import storage
import unittest

class TestFileStorage(unittest.TestCase):
    """ testing functionality of FileStorage Class"""

    def setUp(self):
        """ setting up tests:
        
        """
        obj = {'id': '999-999-999', 'name': 'Walter White'}
        storage_test = FileStorage()
        storage_test.__file_path = 'test_file.json'
        storage_test.reload()
        storage_test.new(obj)
        storage_test.save()
    
    def test_basic(self):
        """ """



class TestStorageInit(unittest.TestCase):
    """ testing """

    def test_exist(self):
        """ """
        pass
