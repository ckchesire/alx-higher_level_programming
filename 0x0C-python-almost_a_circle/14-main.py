#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string(None)
    r = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4, 1, 2)
    dict_list = [r1.to_dictionary(), r2.to_dictionary()]
    json_dict_list = Base.to_json_string([dict_list])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
    print(dict_list)
    print(json_dict_list)
