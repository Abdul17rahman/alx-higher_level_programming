#!/usr/bin/python3
"""
   Module to create a student class
"""


class Student:
    """
       Student - class
       Attributes:
                 to_json(): retrieve a dict rep of student instance
       Args:
           first_name (str): Student's first name
           last_name  (str): Student's last name
           age        (int): Student's age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
