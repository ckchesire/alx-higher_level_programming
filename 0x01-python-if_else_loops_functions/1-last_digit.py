#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
len_str = len(str(number))
last_num = str(number)[len_str-1]

if (number < 0):
    last_num = (int(last_num) * -1)

if int(last_num) > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif int(last_num) < 6 and int(last_num) != 0:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
elif int(last_num) == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
