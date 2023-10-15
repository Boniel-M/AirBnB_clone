#!/usr/bin/python3
import json
import os

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    #def __init__(self):


    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj


   # def save(self):
    #    my_dict = {}
     #   for key, value in FileStorage.__objects.items():
      #      my_dict[key] = value.to_dict()
       # with open(FileStorage.__file_path, "w") as file:
        #    json.dump(my_dict, file)

   # def reload(self):
    #    try:
     #       with open(FileStorage.__file_path, "r") as file:
      #          data = json.load(file)
       # except FileNotFoundError:
        #    pass

    def save(self):
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(my_dict, file)
