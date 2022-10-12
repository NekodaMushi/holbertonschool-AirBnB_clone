#!/usr/bin/python3
"""Entry point of command interpreter"""
import cmd
import argparse
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Terminal like python"""

    prompt = '(hbnb)'
    classes = {"BaseModel"}

    def do_EOF(self, arg):
        """Ctrl-d"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def emptyline(self):
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
        try:
            if args[1]:
                name = f"{args[0]}.{args[1]}"
                if name not in storage.all().keys():
                    # all().keys() according to the "pattern"
                    # of the key we declared here and before
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Deletes an instance based
        on the class name and id"""
        args = line.split()
        dict = storage.all()
        idExist = 0
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            for key, value in dict.copy().items():
                if key == f"{args[0]}.{args[1]}":
                    dict.pop(key)
                    storage.save()
                    idExist = 1
            if idExist == 0:
                print('** no instance found **')

    def do_all(self, line):
        """Prints all strings representation of all
        instances based or not on the class name"""
        args = line.split()
        all_dict = storage.all()
        string_list = []
        if len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
        elif len(args) == 0:
            for value in all_dict.copy().values():
                if value.__class__.__name__ == args[0]:
                    string_list.append(str(value))
            print(string_list)

    def do_update(self, line):
        """
        Updates an instance based on class name
        and id by adding or updating attributes
        Usage:
        update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if len(args) >= 4:
            name = f"{args[0]}.{args[1]}"
            right_type = type(args[2])
            args3 = right_type(args[3])
            args3 = args3.strip('\"')
            setattr(storage.all()[name], args[2], args3)
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif (f"{args[0]}.{args[1]}" not in storage.all().keys()):
            print("** no instance found **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
