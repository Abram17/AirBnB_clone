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

    def do_quit(self, *args):
        """
        exit the program
        """
        return True

    def help_quit(self, *args):
        """
        prints a notice on how to quit
        """
        print("Quit command to exit the program")

    def do_EOF(self, *args):
        """
        end of line
        """
        print()
        return True

    def emptyline(self):
        """
        empty line + ENTER: execute nothing
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
