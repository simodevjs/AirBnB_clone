import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Unit tests for User"""

    def test_user_creation(self):
        """Test creation of User instance"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_attributes(self):
        """Test User specific attributes are strings"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.password, str)

if __name__ == '__main__':
    unittest.main()
