#!/usr/bin/python3
"""Entry point of command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Terminal like python"""

    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """Ctrl-d"""
        return True
    
    def do_quit(self,arg):
        """Ctrl-z"""
        exit()

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
