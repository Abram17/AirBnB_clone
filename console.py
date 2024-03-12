#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    class for the HBNBC cmd
    """
    prompt = "(hbnb)"
    Existing = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def default(self, args):
        """
        ovewrite the default cmd
        """
        words = args.split('.')
        name = words[0]
        func = words[1].split('(')[0]
        methods = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'count': self.do_count
        }
        if func not in methods:
            print(f" **unknown method: {func}** ")
            return False
        else:
            return methods[func](f"{name} {''}")

    def do_quit(self, args):
        """
        exit the program
        """
        return True

    def help_quit(self, args):
        """
        prints a notice on how to quit
        """
        print("Quit command to exit the program")

    def do_EOF(self, args):
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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        """
        cmds = shlex.split(args)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.Existing:
            print("** class doesn't exist **")
        else:
            new = eval(f"{cmds[0]}()")
            storage.save()
            print(new.id)

    def do_show(self, args):
        """
         Prints the string representation of an instance
         based on the class name and id
        """
        cmds = shlex.split(args)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.Existing:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            k = f"{cmds[0]}.{cmds[1]}"
            if k in storage.all():
                print(storage.all()[k])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        cmds = shlex.split(args)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.Existing:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            k = f"{cmds[0]}.{cmds[1]}"
            if k in storage.all():
                del storage.all()[k]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
         Prints all string representation of all instances
         based or not on the class name
        """
        cmds = shlex.split(args)
        if len(cmds) == 0:
            for k, v in storage.all().items():
                print(str(v))
        elif cmds[0] not in self.Existing:
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if k.split(".")[0] == cmds[0]:
                    print(str(v))

    def do_update(self, args):
        """
        Updates an instance
        based on the class name and id
        by adding or updating attribute
        """
        cmds = shlex.split(args)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.Existing:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            k = f"{cmds[0]}.{cmds[1]}"
            if k not in storage.all():
                print("** no instance found **")
            elif len(cmds) < 3:
                print("** attribute name missing **")
            elif len(cmds) < 4:
                print("** value missing **")
            else:
                name = cmds[2]
                val = cmds[3]
                try:
                    val = eval(val)
                except Exception:
                    pass
                setattr(storage.all()[k], name, val)
                storage.all()[k].save()

    def do_count(self, args):
        """
        retrieve the number of instances of a class
        """
        cmds = shlex.split(args)
        if args:
            name = cmds[0]
        num = 0
        if cmds:
            if name in self.Existing:
                for val in storage.all().values():
                    if val.__class__.__name__ == name:
                        num += 1
                print(num)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
