#!/usr/bin/python3
alphabet = ['q', 'e']
for i in range(97, 123):
    if chr(i) not in alphabet:
        print("{}".format(chr(i)), end="")
