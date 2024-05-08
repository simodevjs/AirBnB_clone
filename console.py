#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Simple command processor for HBNB clone."""
    prompt = "(hbnb) "

    def default(self, line):
        """Handle commands that do not match any known commands."""
        parts = line.split('.')
        if len(parts) != 2:
            print(f"*** Unknown syntax: {line}")
            return
        
        class_name, command = parts
        if command.startswith("all()"):
            self.do_all(class_name)
        elif command.startswith("count()"):
            self.do_count(class_name)
        elif command.startswith("show(") and command.endswith(")"):
            instance_id = command[5:-1].strip('"\'')
            self.do_show(class_name, instance_id)
        elif command.startswith("destroy(") and command.endswith(")"):
            instance_id = command[8:-1].strip('"\'')
            self.do_destroy(class_name, instance_id)
        elif command.startswith("update(") and command.endswith(")"):
            args = command[7:-1].split(',')
            if len(args) != 3:
                print("** invalid arguments **")
                return
            instance_id, attribute_name, attribute_value = (arg.strip(' "\'') for arg in args)
            self.do_update(class_name, instance_id, attribute_name, attribute_value)
        else:
            print(f"*** Unknown syntax: {line}")


    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_obj = eval(arg)()  
            new_obj.save()
            print(new_obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, class_name, instance_id):
        """Shows an instance based on the class name and id."""
        if class_name not in ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")
    
    """def do_show(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        obj_key = f"{args[0]}.{args[1]}"
        if obj_key in all_objs:
            print(all_objs[obj_key])
        else:
            print("** no instance found **")"""

    def do_count(self, arg):
        """Counts number of instances of a given class."""
        if arg not in ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return
        count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == arg)
        print(count)

    def do_destroy(self, class_name, instance_id):
        """Destroys an instance based on the class name and id."""
        if class_name not in ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()  # Make sure to save changes to the storage
            print("Instance destroyed.")
        else:
            print("** no instance found **")

    """def do_destroy(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        obj_key = f"{args[0]}.{args[1]}"
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")"""

    def do_all(self, arg):
        """Prints all string representations of all instances based or not on the class name."""
        all_objs = storage.all()
        if arg:
            if not eval(arg):
                print("** class doesn't exist **")
                return
        print([str(obj) for obj in all_objs.values() if not arg or isinstance(obj, eval(arg))])

    def do_update(self, class_name, instance_id, attribute_name, attribute_value):
        """Updates an instance based on the class name and id."""
        if class_name not in ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        obj = all_objs[key]
        if hasattr(obj, attribute_name):
            setattr(obj, attribute_name, attribute_value)
            obj.save()
            print("Instance updated.")
        else:
            print("** attribute not found **")

    """def do_update(self, line):
        args = line.split()
        if len(args) < 2:
            print("** class name missing **" if len(args) == 0 else "** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        all_objs = storage.all()
        obj_key = f"{args[0]}.{args[1]}"
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        setattr(all_objs[obj_key], args[2], args[3])
        all_objs[obj_key].save()"""

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()