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


if __name__ == '__main__':
    unittest.main()
