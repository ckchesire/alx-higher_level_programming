#!/usr/bin/python3
def no_c(my_string):
    s_list = []
    for s in my_string:
        s_list.append(s)
    for c in s_list:
        if c == 'c':
            s_list.remove('c')
        if c == 'C':
            s_list.remove('C')
    result = "".join(s_list)
    return (str(result))
