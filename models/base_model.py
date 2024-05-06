import uuid
import datetime


class BaseModel:
    """A base class for all hbnb models."""

    def __init__(self, **kwargs):
        """Initialize the BaseModel with id, created_at, and updated_at attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        # Manually construct the dictionary string with repr() for clear debugging output.
        ordered_dict = {k: v for k, v in reversed(self.__dict__.items())
                        if k not in ['id', 'created_at', 'updated_at']}
        ordered_dict['updated_at'] = self.updated_at
        ordered_dict['id'] = self.id
        ordered_dict['created_at'] = self.created_at
        self.__dict__ = ordered_dict
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__ }"

    def save(self):
        """Update the updated_at attribute to the current datetime."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Return a dictionary of the instance attributes for serialization,
        including the class name.
        """
        result = {k: v for k, v in reversed(self.__dict__.items())
                  if k not in ['id', 'created_at', 'updated_at']}
        result['__class__'] = self.__class__.__name__  # Add class name
        # Convert datetime attributes to ISO format strings and add them in order.
        result['updated_at'] = self.updated_at.isoformat()
        result['id'] = self.id
        result['created_at'] = self.created_at.isoformat()
        return result
