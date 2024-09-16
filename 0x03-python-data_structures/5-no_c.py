#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        s_list = []
        for s in my_string:
            s_list.append(s)
        for c in s_list:
            if c == 'c':
                s_list.remove('c')
            elif c == 'C':
                s_list.remove('C')
        s_list = "".join(s_list)
        return (s_list)
