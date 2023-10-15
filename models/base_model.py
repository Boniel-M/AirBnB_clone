#!/usr/bin/python3


from datetime import datetime
import uuid
from models.__init__ import storage
from models.engine.file_storage import FileStorage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            my_uuid = str(uuid.uuid4())
            current_datetime = datetime.now()
            self.id = my_uuid
            self.created_at = current_datetime
            self.updated_at = current_datetime
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
