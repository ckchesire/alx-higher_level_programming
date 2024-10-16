#!/usr/bin/python3
"""Module retrieves a dictionary representation of a Student instance
"""


class Student:
    """ Blueprint for class Student
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize instance variables for class

            Args:
                first_name : string of student's first name
                last_name : string of student's last name
                age : students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function to retrieve attributes of student class

            Returns:
                returns a dictionary representation of student instance
        """
        if attrs is None:
            return self.__dict__
        res = {}
        for k, v in self.__dict__.items():
            if k in attrs:
                res[k] = v
        return res
