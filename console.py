#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class """

    prompt = '(hbnb) '

    def emptyline(self):
        print(end="")

    def do_quit(self, *arg):
        """
        exits the command interpreter
        """
        return True

    do_EOF = do_quit

    def do_create(self, *arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Usage:
            create BaseModel
        """
        print(arg)
        if (arg[0] == ''):
            print("** class name missing **")
        elif (arg[0] == 'BaseModel'):
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
