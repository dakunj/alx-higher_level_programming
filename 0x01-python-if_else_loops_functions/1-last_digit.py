#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_digit = number_str[-1]
last_digit = int(last_digit)
if last_digit > 5:
    print("Last digit of", number_str, "is", last_digit, "and is greater than 5")
elif last_digit == 0:
    print("Last digit of", number_str, "is", last_digit, "and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print("Last digit of", number_str, "is", last_digit, "and is less than 6 and not 0")
