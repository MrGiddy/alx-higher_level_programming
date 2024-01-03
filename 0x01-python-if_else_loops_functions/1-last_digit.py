#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(number):
    if type(number) != int:
        raise TypeError

    last_digit = str(number)[-1]
    last_digit = int(last_digit)

    if (number < 0):
        last_digit *= -1

    if (last_digit > 5):
        print(f"Last digit of {number} is {last_digit}", end=" ")
        print(f"and is greater than 5")
    elif (last_digit == 0):
        print(f"Last digit of {number} is {last_digit} and is 0")
    else:
        print(f"Last digit of {number} is {last_digit}", end=" ")
        print(f"and is less than 6 and not 0")


last_digit(number)
