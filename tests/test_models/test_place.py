import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Unit tests for Place"""

    def test_place_creation(self):
        """Test creation of Place instance"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))

if __name__ == '__main__':
    unittest.main()
