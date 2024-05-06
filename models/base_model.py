import uuid
import datetime

class BaseModel:
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        # Manually construct the dictionary string with repr() for clear debugging output.
        ordered_dict = {k: v for k, v in reversed(self.__dict__.items()) if k not in ['id', 'created_at', 'updated_at']}
        ordered_dict['updated_at'] = self.updated_at
        ordered_dict['id'] = self.id
        ordered_dict['created_at'] = self.created_at
        #dict_str = ', '.join(f"'{k}': {repr(v)}" for k, v in ordered_dict.items())
        #return f"[{self.__class__.__name__}] ({self.id}) {{{dict_str}}}"
        return f"[{self.__class__.__name__}] ({self.id}) {ordered_dict}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary of the instance attributes for serialization, including the class name."""
        # Create a dictionary of instance attributes for serialization, including datetime conversion.
        result = {k: v for k, v in reversed(self.__dict__.items()) if k not in ['id', 'created_at', 'updated_at']}
        result['__class__'] = self.__class__.__name__  # Add class name
        # Convert datetime attributes to ISO format strings and add them in order.
        result['updated_at'] = self.updated_at.isoformat()
        result['id'] = self.id
        result['created_at'] = self.created_at.isoformat()
        return result