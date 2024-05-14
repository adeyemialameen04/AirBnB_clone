#!/usr/bin/python3
"""Filestorage model"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @staticmethod
    def all(self):
        return FileStorage.__objects

    @staticmethod
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    @staticmethod
    def save(self):
        obj_dict = {}

        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    @staticmethod
    def relaod(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                json_obj = json.load(file)
                for key, obj_dict in json_obj.items():
                    class_name, obj_id = key.split('.')
                    mudule = 

        except FileNotFoundError:
            pass
