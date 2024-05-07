import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Unit tests for City"""

    def test_city_creation(self):
        """Test creation of City instance"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.name, '')
        self.assertEqual(city.state_id, '')

if __name__ == '__main__':
    unittest.main()
