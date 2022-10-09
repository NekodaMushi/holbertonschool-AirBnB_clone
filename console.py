#!/usr/bin/python3
"""Console- entry point of cmd interpreter"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """let's have fun!!"""
    # Customize prompt right here easily
    prompt = '(hbnb)'

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
