import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Unit tests for Amenity"""

    def test_amenity_creation(self):
        """Test creation of Amenity instance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')

if __name__ == '__main__':
    unittest.main()