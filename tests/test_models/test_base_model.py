import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        """Test that each BaseModel has a unique id"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)
        self.assertNotEqual(model1.id, model2.id)

    def test_to_dict(self):
        """Test that the dictionary representation includes correct keys"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn("id", model_dict)
        self.assertIn("__class__", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
"""
    def test_to_dict_contains_correct_types(self):
        //Test that the dictionary representation contains correct types for datetime fields//
        model = BaseModel()
        model_dict = model.to_dict()
        for key in ["created_at", "updated_at"]:
            self.assertIsInstance(datetime.fromisoformat(model_dict[key]), datetime)
"""

if __name__ == '__main__':
    unittest.main()
