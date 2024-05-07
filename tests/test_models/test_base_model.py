import unittest
from models.base_model import BaseModel
from datetime import datetime
import models

class TestBaseModel(unittest.TestCase):
    """Unit tests for BaseModel"""

    def test_instance_creation(self):
        """Test for correct instance creation"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_time_attributes(self):
        """Test that created_at, updated_at are datetime objects"""
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_save(self):
        """Test the save method"""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

if __name__ == '__main__':
    unittest.main()
