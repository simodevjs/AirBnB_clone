import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Unit tests for Review"""

    def test_review_creation(self):
        """Test creation of Review instance"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

if __name__ == '__main__':
    unittest.main