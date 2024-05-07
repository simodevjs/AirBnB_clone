#!/usr/bin/python3
"""Unit tests for the HBNBCommand class."""
import unittest
from consoleold1 import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Tests for the HBNBCommand command interpreter."""

    def test_quit(self):
        """Test that 'quit' command exits the interpreter."""
        console = HBNBCommand()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        """Test that 'EOF' command exits the interpreter."""
        console = HBNBCommand()
        self.assertTrue(console.onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
