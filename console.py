#!/usr/bin/python3

import cmd

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
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
