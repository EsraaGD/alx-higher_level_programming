#!/usr/bin/python3
import json
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)

        with open(filename, 'w') as file:
            json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            )
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10)
        else:
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dic = cls.from_json_string(json_string)
                inst = [cls.create(**dictionary) for dictionary in dic]
                return inst
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.csv".format(cls.__name__)

        with open(filename, mode='w') as file:
            writer = csv.writer(file)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)
        inst_list = []

        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        inst = cls(id=int(row[0]), width=int(row[1]),
                                height=int(row[2]),x=int(row[3]), y=int(row[4]))
                    elif cls.__name__ == "Square":
                        inst = cls(id=int(row[0]), size=int(row[1]),
                                   x=int(row[2]), y=int(row[3]))
                    inst_list.append(inst)
        except FileNotFoundError:
            pass

        return inst_list
