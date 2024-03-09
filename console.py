#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd
import sys
import re
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
	"""
	command line interpreter class
	"""
	prompt = "(hbnb)"

	def do_quit(self, arg):
		"""
		exit the program
		"""

		return True

	def do_EOF(self, arg):
		"""
		end of file
		"""

		print()
		return True

	def do_create(self, arg):
		"""
		Creates a new instance of BaseModel
		"""
		if arg == "" | arg is None:
			print("** class name missing **")
		elif arg not in storage.existing():
			print("** class doesn't exist **")
		else:
			o = storage.existing()[arg]()
			o.save()
			print(o.id)

	def do_show(self, arg):
		"""
		Prints the string representation of an instance based on the class name
		"""
		if arg != "" | arg is not None:
			info = arg.split(".")
			if info[0] not in storage.existing():
				print("** class doesn't exist **")
			elif len(info) < 2:
				print("** instance id missing **")
			else:
				key = f"{info[0]}.{info[1]}"
				if key not in storage.all():
					print("** no instance found **")
				else:
					print(storage.all()[key])
		else:
			print("** class name missing **")

	def do_destroy(self, arg):
		"""
		Deletes an instance based on the class name and id
		"""
		if arg != "" | arg is not None:
			info = arg.split(".")
			if info[0] not in storage.existing():
				print("** class doesn't exist **")
			elif len(info) < 2:
				print("** instance id missing **")
			else:
				key = f"{info[0]}.{info[1]}"
				if key not in storage.all():
					print("** no instance found **")
				else:
					del storage.all()[key]
					storage.save()
		else:
			print("** class name missing **")

if __name__ == "__main__":
	HBNBCommand().cmdloop()
