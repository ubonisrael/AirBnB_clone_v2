#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        # if the class is not provided as an argument
        # return every object
        if cls is None:
            return FileStorage.__objects
        # else, search the FileStorage.__objects and copy matching
        # objects to a new dict, then return dict
        cls_dict = {}
        for my_obj in FileStorage.__objects:
            myobj_cls = my_obj.split('.')[0]
            if myobj_cls == cls.__name__:
                cls_dict[my_obj] = FileStorage.__objects[my_obj]
        return cls_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an obj for __objects if it's inside"""
        if obj is None:
            return
        # set an integer to zero to indicate an initial state of non-existence
        id_exists = 0
        del_obj = None
        for myobj in FileStorage.__objects:
            myobj_id = myobj.split('.')[1]
            if myobj_id == obj.id:
                # if the id exists, set id_exists to 1
                # and set del obj to the current object
                id_exists = 1
                del_obj = myobj
                break
        # if id_exists is true ie 1, delete
        if id_exists == 1:
            del (FileStorage.__objects[del_obj])
