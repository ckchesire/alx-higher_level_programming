#!/usr/bin/python3
class Student:
    """ Blueprint for class Student
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize instance variables for class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function to retrieve attributes of student class
        """
        return self.__dict__
