#!/usr/bin/python3

import json
import cmd
from models.base_model import BaseModel
import models.__init__
from models import storage

class HBNBCommand(cmd.Cmd):
    '''Entry point'''

    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        """Quit when Ctr+z is hit"""
        return True

    def emptyline(self):
        """Overrides the default empty line. Empty line executes nothing"""

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it(to the JSON file) and prints it"""
        base1 = BaseModel()
        FileStorage.new()
        with open(FileStorage._file, "w") as file:
            FileStorage.save()
            print(base.id)
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
