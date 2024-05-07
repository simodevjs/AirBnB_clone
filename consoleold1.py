#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    """Simple command processor for the HBNB clone."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle EOF signal to exit the program."""
        print()  # Ensure a newline is printed before exiting
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()