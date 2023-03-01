#!/usr/bin/python3
"""shebang"""
import cmd

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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
