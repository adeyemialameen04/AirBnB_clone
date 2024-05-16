#!/usr/bin/python3
"""Documenting the console module"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Documentation for the console"""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        if arg == "":
            print("** class name missing **")
            return

        name = arg.split()[0]
        cls = globals().get(name)
        if cls is None:
            print("** class doesn't exist **")
            return
        obj = cls()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
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
        print(storage.all()[key])

    def do_destroy(self, arg):
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
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
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

        for key, value in storage.all().items():
            if key.startswith(name):
                objs.append(str(value))
        print(objs)

    def do_update(self, arg):
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


    def emptyline(self):
        """Does nothing."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
