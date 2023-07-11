#!/usr/bin/python3
"""
   Module to create a student class with student to JSON filter attr
"""


class Student:
    """
       Student - class
       Attributes:
                 to_json(): retrieve a dict rep of student instance
                 reload_from_json(): replace all attributes of the student
                                          instance.
                 first_name (str): Student's first name
                 last_name  (str): Student's last name
                 age        (int): Student's age
       Args:
           first_name (str): Student's first name
           last_name  (str): Student's last name
           age        (int): Student's age
    """
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        if attrs is not None:
            attrs.sort()
            new_dict = {}
            for item in attrs:
                if self.__dict__.__contains__(item):
                    new_dict[item] = self.__dict__.get(item)
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
