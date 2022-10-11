#!/usr/bin/python3
"""Console- entry point of cmd interpreter"""
import cmd
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
