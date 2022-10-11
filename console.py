#!/usr/bin/python3
"""Entry point of command interpreter"""
import cmd
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

    def do_show(self, args):
        """
        String representation: provide class name and id
        Usage: show <ClassName <id>
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        if args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        className = f"{args[0]}, {args[1]}"

    def do_destroy(self, args):
        """Deletes an instance based
        on the class name and id"""
        dict = storage.all()
        idExist = 0
        if len(args) == 0:
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            for key, value in dict.items():
                if key == f"{args[0].args[1]}":
                    dict.pop(key)
                    storage.save()
                    idExist = 1
            if idExist == 0:
                print('** no instance found **')

    def do_all(self, args):
        """Prints all strings representation of all
        instances based or not on the class name"""
        all_dict = storage.all()
        string_list = []
        if len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
        for value in all_dict.values():
            if value.__class__.__name__ == args[0]:
                string_list.append(str(value))
        print(string_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
