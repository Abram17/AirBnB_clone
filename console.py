#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd
import re
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
			info = arg.split(" ")
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
			info = arg.split(" ")
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

	def do_all(self, arg):
		"""
		 Prints all string representation of all instances based or not on the class name
		"""
		list = []

		if arg != "" | arg is not None:
			if arg not in storage.existing():
				print("** class doesn't exist **")
			else:
				for key, value in storage.all().items():
					clas_name, inst_id = key.split(" ")
					if arg == clas_name:
						list.append(str(value))
				print(list)
		else:
			for key, value in storage.all().items():
				list.append(str(value))
			print(list)

	def do_update(self, arg):
		"""
		save the change into the JSON file
		"""
		if arg != "" | arg is not None:
			r = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
			m = re.search(r, arg)
			clas_name = m.group(1)
			uid = m.group(2)
			attr = m.group(3)
			val = m.group(4)
			if not m:
				print("** class name missing **")
			elif clas_name not in storage.existing():
				print("** class doesn't exist **")
			elif uid is None:
				print("** instance id missing **")
			else:
				key = f"{clas_name}.{uid}"
				if key not in storage.all():
					print("** no instance found **")
				elif not attr:
					print("** attribute name missing **")
				elif not val:
					print("** value missing **")
				else:
					put = None
					if not re.search('^".*"$', val):
						if '.' in val:
							put = float
						else:
							put = int
					else:
						val = val.replace('"', '')
					attributes = storage.attributes()[clas_name]
					if attr in attributes:
						val = attributes[attr](val)
					elif put:
						try:
							val = put(val)
						except ValueError:
							pass
						setattr(storage.all()[key], attr, val)
						storage.all()[key].save()
		else:
			print("** class name missing **")
			return

	def do_count(self, line):
		"""
		Counts the instances of a class.
		"""
		count = 0
		for key in storage.all().keys():
			class_name, inst_id = key.split(".")
			if line == class_name:
				count += 1
		print(count)

	def emptyline(self):
		pass

if __name__ == "__main__":
	HBNBCommand().cmdloop()
