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


if __name__ == "__main__":
    new_model = BaseModel()
    new_model.name = "New Model"
    new_model.num = 7
    print(new_model)
    new_model.save()
    print(new_model)
    new_model_json = new_model.to_dict()
    print(new_model_json)
    print("json of this model:")
    for key in new_model_json.keys():
        print(f"\t{key}: ({type(new_model_json[key])}) - {new_model_json[key]}")
