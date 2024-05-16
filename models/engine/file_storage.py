#!/usr/bin/python3
"""Filestorage model"""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    dict_obj = json.loads(file.read())
                except json.JSONDecodeError:
                    return
                for key, value in dict_obj.items():
                    class_name = key.split(".")[0]
                    obj = globals()[class_name](**dict_obj[key])
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
