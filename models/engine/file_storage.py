#!/usr/bin/python3
"""
Defines a module to serialize and deserialize
instances.
"""
from json import dumps, loads
from os.path import isfile


class FileStorage:
    """
    Define members for serializing instances
    to a JSON file and deserializes JSON file
    to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the objects stored """
        return (FileStorage.__objects)

    def new(self, obj):
        """ Sets the value for an object """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes objects to a JSON file """
        objects = {}
        for key, value in FileStorage.__objects.items():
            objects[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(dumps(objects))

    def reload(self):
        """ Deserializes the JSON file into object(s) """
        objects = {}

        if (isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as file:
                objects = loads(file.read())
            from models.base_model import BaseModel
            for key, value in objects.items():
                class_name = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(class_name + "(**value)")
