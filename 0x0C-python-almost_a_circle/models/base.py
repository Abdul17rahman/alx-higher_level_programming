#!/usr/bin/python3

"""
    Base Class Module
"""
import json


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
        js_st = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(json.dumps(json.loads(js_st), separators=(",", ":")))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of JSON str rep"""
        if not json_string or json_string is None:
            return []
        return list(json.loads(json_string))
