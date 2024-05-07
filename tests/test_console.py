import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Unit tests for the HBNB console command interpreter"""

    def test_quit_command(self):
        """Test the quit command exits"""
        with patch('sys.stdout', new_callable=StringIO) as output:
            cmd = HBNBCommand()
            self.assertTrue(cmd.onecmd("quit"))

    def test_EOF_command(self):
        """Test the EOF command exits"""
        with patch('sys.stdout', new_callable=StringIO) as output:
            cmd = HBNBCommand()
            self.assertTrue(cmd.onecmd("EOF"))
"""Test the create command functionality
    def test_create_command(self):
        with patch('sys.stdout', new_callable=StringIO) as output:
            cmd = HBNBCommand()
            cmd.onecmd("create BaseModel")
            self.assertIn('** class name missing **', output.getvalue() or cmd.onecmd("create"))"""

if __name__ == '__main__':
    unittest.main()
