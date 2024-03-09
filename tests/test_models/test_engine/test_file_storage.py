#!/usr/bin/python3
""" unittest for file_storage.py """
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """ testing functionality of FileStorage Class"""

    def setUp(self):
        """ setting up tests:
            - creating dictionary to be saved to used.
            - creating FileStorage object.
            - changing name of file to write data on.
        """
        self.obj = {'__class__': 'BaseModel',
                    'id': '999-999-999',
                    'name': 'Walter White'}
        self.storage_test = FileStorage()
        self.storage_test.testfilepath = 'test_file.json'
        self.storage_test.testobjects = {}

    def tearDown(self):
        """ returning to original storage file path """
        self.storage_test.testfilepath = 'file.json'

    def test_basic(self):
        """ testing basic functionality of FileStorage class """
        with self.subTest('[1] testing initialization of FileStorage object'):
            self.assertTrue(isinstance(self.storage_test, FileStorage))
            self.assertTrue(isinstance(self.storage_test.testfilepath,
                                       str))
            self.assertTrue(isinstance(self.storage_test.testobjects, dict))
            self.assertTrue(self.storage_test.testobjects == {})

        with self.subTest('[2] testing FileStorage class methods'):
            dict_key = f"{self.obj['__class__']}.{self.obj['id']}"
            self.storage_test.new(self.obj)
            self.assertEqual(self.obj,
                             self.storage_test.testobjects[dict_key])

        with self.subTest('[3] testing save() and reload()'):
            self.storage_test.save()
            self.storage_test.testobjects = {}
            self.storage_test.reload()
            self.assertEqual(self.obj,
                             self.storage_test.testobjects[dict_key])
