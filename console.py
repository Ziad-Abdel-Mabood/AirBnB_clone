#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    """ Command interpreter class """

    prompt = '(hbnb) '
    all_models = {'BaseModel': BaseModel,
                  'User': User,
                 }

    def emptyline(self):
        print(end="")

    def do_quit(self, *arg):
        """
        exits the command interpreter
        """
        return True

    do_EOF = do_quit

    def do_create(self, model):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Usage:
            create BaseModel
        """
        if (model == ''):
            print("** class name missing **")
            return
        elif (model in self.all_models.keys()):
            new_obj = self.all_models[model]()
            new_obj.save()
            print(new_obj.id)
            return
        elif (model not in self.all_models.keys()):
            print("** class doesn't exist **")
            return
    
    def do_show(self, model='', model_id=''):
        """
        prints the string representation of an instance
        based on the class name and id.

        Usage:
            show BaseModel 1234-1234-1234
        """
        all_objs = storage.all()
        print(model)
        print(model_id)
        if (model == ''):
            print("** class name missing **")
            return
        elif(model_id == ''):
            print("** instance id missing **")
            return

        key = f"{model}.{model_id}"
        if(key not in storage.all()):
            print("** no instance found **")
            return
        elif(key in all_objs):
            print(all_objs[key])

    def do_all(self, *arg):
        """
        Prints all string representation of all instances based 
        or not on the class name.
        Usage:
            all BaseModel
                or 
            all. 
        """
        if (arg[0] == ''):
            pass
                         


if __name__ == '__main__':
    HBNBCommand().cmdloop()
