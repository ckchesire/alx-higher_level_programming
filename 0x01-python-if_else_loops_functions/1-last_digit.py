#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
len_str = len(str(number))
last_number = str(number)[len_str-1]

if int(last_number) > 5:
    print(f"Last digit of {number} is {last_number} and is greater than 5")
elif int(last_number) < 6 and int(last_number) != 0:
    print(f"Last digit of {number} is {last_number} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_number} and is 0")
