#!/usr/bin/python3
"""
conains the BaseModel class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        """
        initilizes the BaseModel
        """
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
        this_dict[__class__] = self.__class__.__name__
        this_dict["created_at"] = self.created_at.isoformat()
        this_dict["updated_at"] = self.updated_at.isoformat()

        return this_dict

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
