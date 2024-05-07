import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Unit tests for State"""

    def test_state_creation(self):
        """Test creation of State instance"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, '')

if __name__ == '__main__':
    unittest.main()
