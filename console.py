#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class for the HBNBC cmd
    """
    prompt = "(hbnb)"

    def quit_func(self, arg):
        """
        exit the program
        """
        return True

    def EOF(self, arg):
        """
        end of line
        """
        print()
        return True

    def helper(self, arg):
        """
        notice to help you quit
        """
        print("typy quit to exit")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
