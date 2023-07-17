#!/usr/bin/python3

"""
    Base Class Module
"""
import json
import csv


class Base:
    """
    This is where our classes inherit from.
        Attr:
            nb_objects: Private class attribute

        Methods:
            Constructor: Initializes the class
            valid_input: Validates inputs
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing Base"""
        if isinstance(id, int) and id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Function to help validate input
    def valid_input(self, name, value, val_typ="cor"):
        """
            Validates the input values

            Args:
                name: Name of the field/attribute
                value: Value of the field/attribute
                val_typ: Dimension or Coordinates

            Raises:
                TypeError: If the value is not an int
                ValueError: If the value is less than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if val_typ == "dime":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string of dicts """
        dict_list = []
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        for dictionary in list_dictionaries:
            dict_list.append(dictionary)
        return json.dumps(dict_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON to a file """
        filename = cls.__name__ + ".json"
        if list_objs:
            js_st = cls.to_json_string([obj.to_dictionary()
                                       for obj in list_objs])
        else:
            js_st = cls.to_json_string([])
        with open(filename, 'w') as file:
            file.write(js_st)

    @classmethod
    def create(cls, **dictionary):
        """ Returns a created Instance """
        inst = cls(1, 3)
        inst.update(**dictionary)
        return inst

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of JSON str rep"""
        if not json_string or json_string is None:
            return []
        return list(json.loads(json_string))

    @classmethod
    def load_from_file(cls):
        """ Create new instances from file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                loaded_data = f.read()
            list_objs = cls.from_json_string(loaded_data)
            return [cls.create(**obj) for obj in list_objs]
        except Exception:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """ Load from a file """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.reader(f)
            return [cls.create(**dictionary) for item in reader]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
           save_to_file_csv - write JSON string representation of list_objs
                              to a file
        """
        filename = cls.__name__ + ".csv"
        if list_objs:
            csv_data = [obj.to_dictionary() for obj in list_objs]
        else:
            csv_data = []

        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(csv_data)
