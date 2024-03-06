#!/usr/bin/python3
""" the base class; defines all common attr/methods for other classes """
import datetime
import uuid


class BaseModel:
    """ BaseModel class which will pass on common attr/methods for all
        other classes in the project.
        Can be created with extra attributes at initialization
        or recreated from a dict using kwargs.

        Attributes:
            id:             unique id for each instance.
            created_at:     time and date of creating the instance.
            updated_at:     time and date of the last change applied
                            to the instance.
    """

    def __init__(self, *args, **kwargs):
        """ constructor method """
        if kwargs:  # accepting attributes from kwargs to recreate instance
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        else:       # if kwargs is empty create a new model
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """ string representation of the object """
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates the public instance attribute
            updated_at with the current datetime """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
