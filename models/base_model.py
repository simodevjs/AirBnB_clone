import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class that defines all common attributes and methods for other classes.
    """

    def __init__(self):
        """
        Initialize a new instance of BaseModel
        """
        self.id = str(uuid.uuid4())  # Unique identifier for each instance
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Provide a string representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' attribute to the current datetime 
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary with the instance's attributes
        """
        # Specific attributes with their direct values
        spec_attr = {
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }

        # Collect dynamic attributes, exclude any specific ones to avoid duplication
        dynam = {k: v for k, v in reversed(self.__dict__.items()) if k not in spec_attr}

        # Initialize final dictionary in LIFO, Add specific attributes 
        final_dict = {}
        for key, value in dynam.items():
            final_dict[key] = value
        for key, value in spec_attr.items():
            if key not in final_dict:
                final_dict[key] = value

        return final_dict
