#!/usr/bin/python3
"""
module that contains the FileStorage class
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
         returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        objs = FileStorage.__objects
        o_dict = {}
        for obj in objs.keys():
            o_dict[obj] = objs[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(o_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    o_dict = json.load(f)
                    for k, v in o_dict.items():
                        class_name, o_id = k.split(".")
                        cls = eval(class_name)
                        ins = cls(**v)
                        FileStorage.__objects[k] = ins
                except Exception:
                    pass
