## 0x01. Python - if/else, loops, functions

### 0-positive_or_negative.py
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

* You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/0-positive_or_negative_py)
* The variable number will store a different value every time you will run this program
* You don’t have to understand what import, random. randint do. Please do not touch this code
* The output of the program should be:
    * The number, followed by
    - if the number is greater than 0: is positive
    - if the number is 0: is zero
    - if the number is less than 0: is negative
- followed by a new line

### 1-last_digit.py
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number

* You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/1-last_digit_py)
* The variable number will store a different value every time you will run this program
* You don't have to understand what import, random.randint do.
* The output of the program should be:
    * The string Last digit of, followed by:
    * the number, followed by
    * the string is, followed by the last digit of number, followed by
    * if the last digit is > 5: the string and is greater than 5
    * if the last digit is 0: the string and is 0
    * if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
    * followed by a new line

### 2-print_alphabet.py
Write a program that prints the ASCII alphabet, in lowercase, not followed by the new line.

* You can only use one print functon with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module

### 3-print_alphabt.py
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

* Print all the letters except q and e
* You can only use one print function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module

### 4-print_hexa.py
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the followint example)

* You can only use one print function with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

```
guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$
```
### 5-print_comb2.py
Write a program that prints numbers from 0 to 99.

* Numbers must be separated by ,, followed by a space
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 2 print functions with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

### 6-print_comb3.py
Write a program that prints all possible different combinations of two digits.

* Numbers must be separated by ,, followed by a space
* The two digits must be different
* 01 and 10 are considered the same combination of the two digits 0 and 1
* Print only the smallest combination of two digits
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 3 print functions with string format
* You can only use no more than 2 loops in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module

### 7-islower.py
Write a function that checks for lowercase character.
* Prototype: def is lower(c):
* Returns True if c is loercase
* Returns False otherwise
* You are not allowed to import any module
* YOu are not allowed to use str.upper() and str.isupper()
* [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

You don't need to uderstand __import__
```
guillaume@ubuntu:~/0x01$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

guillaume@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
guillaume@ubuntu:~/0x01$ 
```

### 8-uppercase.py
Write a function that prints a string in uppercase followed by a new line.

* Prototype: def uppercase(str):
* You can only use no more than 2 print functions with string format
* You can only use one loop in your code
* You are not allowed to import any module
* You are not allowed to use str.upper() and str.isupper()
* Tips: ord()

You don’t need to understand __import__

### 9-print_last_digit.py
Write a function that prints the last digit of a number.

* Prototype: def print_last_digit(number):
* Returns the value of the last digit
* You are not allowed to import any module
* You don’t need to understand __import__

### 10-add.py
Write a function that adds two integers and returns the result.

* Prototype: def add(a, b):
* Returns the value of a + b
* You are not allowed to import any module
* You don’t need to understand __import__

### 11-pow.py
Write a function that computes a to the power of b and return the value.
* Prototype: def pow(a, b):
* Returns the value of a ^ b
* You are not allowed to import any module
You don’t need to understand __import__

### 101-remove_char_at.py
Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
* Prototype: def remove_char_at(str, n):
* You are not allowed to import any module
You don’t need to understand __import__
