import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage"""

    def setUp(self):
        """Clean up or setup the environment before each test"""
        self.storage = FileStorage()

    def test_new(self):
        """Test adding a new object to storage"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test saving objects to file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Test reloading objects from file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()
