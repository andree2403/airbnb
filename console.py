#!/usr/bin/python3
"""shebang"""
import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    class_names = [
        "BaseModel",
        "User",
        "State",
        "Review",
        "Place",
        "City",
        "Amenity"
    ]

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """End of File to exit file."""
        return True

    def do_emptyline(self):
        """method so it should not execute anything"""
        pass

    def do_create(self, line):
        """create an instance"""
        if not line:
            print("** class name missing **")
            return
        if line not in self.class_names:
            print("** class doesn't exist **")
            return
        else:
            x = eval("{}()".format(line))
            storage.save()
            print("{}".format(x.id))

    def do_show(self, line):
        linesplit = line.split(" ")
        if not line:
            print("** class name missing **")
            return
        if linesplit[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(linesplit) == 1:
            print("** instance id missing **")
            return
        try:
            line = line.replace(' ', '.')
            all_obj = storage.all()
            obj = all_obj[line]
            print(obj)
        except Exception:
            print("** no instance found **")

    def do_destroy(self, line):
        linesplit = line.split(" ")
        if not line:
            print("** class doesn't exis")
            return
        if linesplit[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(linesplit) == 1:
            print("** instance id missing **")
            return
        try:
            line = line.replace(' ', '.')
            all_obj = storage.all()
            del all_obj[line]
            storage.save()
        except Exception:
            print("** no instance found **")

    def do_all(self, line):
        if not line:
            obct = []
            all_obj = storage.all()
            for items in all_obj.values():
                obj_list.append(str(items))
            print(obj_list)
            return
        if line in self.class_names:
            obct = []
            all_obj = storage.all()
            for items in all_obj.values():
                obj_list.append(str(items))
            print(obj_list)
            return
        else:
            print("** class doesn't exist **")

    def do_

if __name__ == '__main__':
    HBNBCommand().cmdloop()
