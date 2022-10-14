#!/usr/bin/python3
"""Entry point of command interpreter"""
import cmd
import json
import models
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Terminal like python"""

    prompt = '(hbnb)'
    classes = {"BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"}
    list_func = {"create", "show", "destroy", "all", "update", "count"}

    def precmd(self, args):
        """
        ** supercharge precmd **
        Hook method executed just before the cmd line interpretation
        With this method, we can "rewrite" the command entered
        Purpose: Parse the input, organize arguments,
        and return the value to be used as a command
        """
        if '.' in args and '(' in args and ')' in args:
            a = args.split('.')
            b = a[1].split('(')
            arg = b[0].split(')')
            if a[0] in HBNBCommand.classes and b[0] in HBNBCommand.list_func:
                args = b[0] + ' ' + a[0]
        return args

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
        if len(line) > 0 and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            lst = []
            all_dict = storage.all()
            for val in all_dict.values():
                if len(line) > 0 and val.__class__.__name__ == args[0]:
                    lst.append(val.__str__())
                elif len(line) == 0:
                    lst.append(val.__str__())
            print(lst)

    def do_update(self, line):
        """
        Updates an instance based on class name
        and id by adding or updating attributes
        Usage:
        update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if f"{args[0]}.{args[1]}" not in storage.all().keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False
        if len(args) == 4:
            name = f"{args[0]}.{args[1]}"
            right_type = type(args[2])
            args3 = args[3]
            args3 = args3.strip('"')
            setattr(storage.all()[name], args[2], right_type(args3))
            storage.all()[name].save()

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class
        """
        num = 0
        all_inst = storage.all()
        for k in all_inst.keys():
            real_key = k.split('.')
            if real_key[0] == arg:
                num += 1
        print(num)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
