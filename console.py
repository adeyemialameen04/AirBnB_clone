#!/usr/bin/python3
"""Documenting the console module"""
import cmd
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """Documentation for the console"""
    methods = ["all()", "count()"]

    prompt = "(hbnb) "

    def parse_arg(self, arg):
        args = shlex.split(arg)
        argc = len(args)
        if argc == 0:
            print("** class name missing **")
            return None, None, None

        name = args[0]
        cls = globals().get(name)
        if cls is None:
            print("** class doesn't exist **")
            return None, None, None

        if argc < 2:
            return cls, None, None

        inst_id = args[1]
        key = f"{name}.{inst_id}"
        if key not in storage.all():
            print("** no instance found **")
            return None, None, None

        return cls, inst_id, args[2:]

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class."""
        cls, _, _ = self.parse_arg(arg)
        if cls:
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Shows an inst of a class."""
        cls, inst_id, _ = self.parse_arg(arg)
        if inst_id is None and cls is not None:
            print("** instance id missing **")
            return
        if cls and inst_id:
            key = f"{cls.__name__}.{inst_id}"
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroys an inst of a class."""
        cls, inst_id, _ = self.parse_arg(arg)
        if inst_id is None and cls is not None:
            print("** instance id missing **")
            return
        if cls and inst_id:
            key = f"{cls.__name__}.{inst_id}"
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Gets all."""
        args = shlex.split(arg)
        argc = len(args)
        objs = []
        if argc == 0:
            for obj in storage.all().values():
                objs.append(str(obj))
            print(objs)
            return

        name = args[0]
        cls = globals().get(name)
        if cls is None:
            print("** class doesn't exist **")
            return

        cls.all(self, name)

    def do_update(self, arg):
        """Updates """
        args = shlex.split(arg)
        argc = len(args)
        if argc == 0:
            print("** class name missing **")
            return
        name = args[0]
        cls = globals().get(name)
        if cls is None:
            print("** class doesn't exist **")
            return

        if argc < 2:
            print("** instance id missing **")
            return

        ist_id = args[1]
        key = f"{name}.{ist_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        if argc < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]

        if argc < 4:
            print("** value missing **")
            return

        attr_val = args[3]

        obj = storage.all()[key]
        setattr(obj, attr_name, attr_val)
        obj.save()

    def default(self, arg):
        match = re.match(r"(\w+)\.(\w+)\((.*)\)", arg)
        match_tup = match.groups()
        argc = len(match_tup)
        if argc == 0:
            print("** class name missing **")
            return

        if match:
            name, method, method_args = match.groups()
            cls = globals().get(name)
            if cls is None:
                print("** class doesn't exist **")
                return

            if method == "all":
                cls.all(self, name)
            elif method == "count":
                cls.count(self, name)
            elif method == "show":
                inst_id = method_args.strip('"\'')
                key = f"{cls.__name__}.{inst_id}"
                if key not in storage.all():
                    print("** instance id missing **")
                    return
                print(storage.all()[key])


    def emptyline(self):
        """Does nothing."""
        pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()
