import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            temp_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(temp_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                temp_dict = json.load(f)
                for key, value in temp_dict.items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
