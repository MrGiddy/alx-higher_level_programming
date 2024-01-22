# 0x05. Python - Exceptions

# Resources
**Read or watch:**

* [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4) (starting at minute 7)

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* Why Python programming is awesome
* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception

# Tasks

### 0-safe_print_list.py
Write a function that prints x elements of a list.

* Prototype: def safe_print_list(my_list=[], x=0):
* my_list can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* x represents the number of elements to print
* x can be bigger than the length of my_list
* Returns the real number of elements printed
* You have to use try: / except:
* You are not allowed to import any module
* You are not allowed to use len()
