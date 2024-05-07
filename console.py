#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command processor for HBNB clone."""

    prompt = "(hbnb) "  # Custom command prompt
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True  # Returning True exits the cmdloop
    def do_EOF(self, arg):
        """Exit the program when receiving EOF (End of File) signal."""
        print()  # Print a newline for clean exit
        return True  # Returning True exits the cmdloop
    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
