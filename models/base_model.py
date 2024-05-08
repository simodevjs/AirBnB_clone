import uuid
import datetime
import models


class BaseModel:
    """A base class for all hbnb models."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel id, created_at, and updated_at attr."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        # Convert string datetime to datetime object
                        value = datetime.datetime.fromisoformat(value)
                    setattr(self, key, value)
        models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        ordered_dict = {k: v for k, v in reversed(self.__dict__.items())
                        if k not in ['id', 'created_at', 'updated_at']}
        if hasattr(self, 'updated_at'):
            ordered_dict['updated_at'] = self.updated_at
        if hasattr(self, 'id'):
            ordered_dict['id'] = self.id
        if hasattr(self, 'created_at'):
            ordered_dict['created_at'] = self.created_at
        self.__dict__ = ordered_dict
        if hasattr(self, 'id'):
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        else:
            return f"[{self.__class__.__name__}] {self.__dict__}"

    def save(self):
        """Update the updated_at attribute to the current datetime."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary of the instance attributes for serialization."""
        result = {k: v for k, v in reversed(self.__dict__.items())
                  if k not in ['id', 'created_at', 'updated_at']}
        result['__class__'] = self.__class__.__name__
        result['updated_at'] = self.updated_at.isoformat()
        result['id'] = self.id
        result['created_at'] = self.created_at.isoformat()
        return result
