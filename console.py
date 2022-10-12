#!/usr/bin/python3
"""Console- entry point of cmd interpreter"""
import cmd
import argparse
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """let's have fun!!"""
    # Customize prompt right here easily
    prompt = '(hbnb)'
    classes = {"BaseModel"}

    def do_EOF(self, line):
        """Ctrl^D exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(1)

    def emptyline(self):
        """empty line + ENTER
        won't execute anything"""
        pass

    def do_create(self, args):
        """
        Creates a new instance defined by User,
        Saves to the JOHNSON file and prints(id)
        Usage: create <ClassName>
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        String representation: provide class name and id
        Usage: show <ClassName <id>
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        # creates a list of string to use argv system
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if args[1]:
            name = "{}.{}".format(args[0], args[1])
            if name not in storage.all().keys():
                # all().keys() according to the "pattern"
                # of the key we declared here and before
                print("** no instance found **")
            else:
                print(storage.all())
        else:
            print("** instance id missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
