#!/usr/bin/python3
"""
conains the BaseModel class
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        initilizes the BaseModel

        Args:
            -*args: arguments
            -**kwargs: key values of args
        """
        if kwargs:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.\
                        strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.\
                        strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary containing:
        all keys/values of __dict__ of the instance
        """
        this_dict = self.__dict__.copy()
        this_dict["__class__"] = self.__class__.__name__
        this_dict["created_at"] = self.created_at.isoformat()
        this_dict["updated_at"] = self.updated_at.isoformat()

        return this_dict

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
