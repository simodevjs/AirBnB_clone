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
        Return a dictionary containing all keys/values of the instance's __dict__,
        """
        dictionary = {'__class__': self.__class__.__name__}
        dictionary.update({
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        })
        dictionary.update({k: v for k, v in self.__dict__.items() if k not in dictionary})
        return dictionary

