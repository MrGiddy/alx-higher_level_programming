# 0x08. Python - More Classes and Objects

# Resources
**Read or watch**:

* [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” (excluded))
* [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
* [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
* [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php) (Mainly the last part “Public instead of Private Attributes”)
* [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

## General
* Why Python programming is awesome
* What is OOP
* “first-class everything”
* what is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* What are the special __str__ and __repr__ methods and how to use them
* What is the difference between __str__ and __repr__
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

# Tasks

### 0. Simple rectantle - [0-rectangle.py](https://github.com/MrGiddy/alx-higher_level_programming/blob/main/0x08-python-more_classes/0-rectangle.py)
Write an empty class Rectangle that defines a rectangle:

You are not allowed to import any module
```
guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/0x08$ 
```
** No test cases needed **

### 1. Real definition of a rectangle - [1-rectangle.py](https://github.com/MrGiddy/alx-higher_level_programming/blob/main/0x08-python-more_classes/1-rectangle.py)
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

* Private instance attribute: width:
    * property def width(self): to retrieve it
    * property setter def width(self, value): to set it:
        * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
        * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
    * property def height(self): to retrieve it
    * property setter def height(self, value): to set it:
        * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
        * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x08$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/0x08$ 
```
**No test cases needed**

### 2. Area and Perimeter - ([2-rectangle.py])(https://github.com/MrGiddy/alx-higher_level_programming/blob/main/0x08-python-more_classes/2-rectangle.py)

Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

Private instance attribute: width:
    * property def width(self): to retrieve it
    * property setter def width(self, value): to set it:
        * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
        * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
    * property def height(self): to retrieve it
    * property setter def height(self, value): to set it:
        * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
        * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter:
    * if width or height is equal to 0, perimeter is equal to 0
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x08$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$ 
```
**No text cases needed**

### 3. String Representation - ([3-rectangle.py](https://github.com/MrGiddy/alx-higher_level_programming/blob/main/0x08-python-more_classes/3-rectangle.py))
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

* Private instance attribute: width:
    * property def width(self): to retrieve it
    * property setter def width(self, value): to set it:
        * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
        * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
    * property def height(self): to retrieve it
    * property setter def height(self, value): to set it:
        * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
        * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter:
    * if width or height is equal to 0, perimeter has to be equal to 0
* print() and str() should print the rectangle with the character #: (see example below)
    * if width or height is equal to 0, return an empty string
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x08$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
guillaume@ubuntu:~/0x08$ 
```
**Object address can be different**
**No test cases needed**

### 4. Eval is magic - ([4-rectangle.py]())
Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)

* Private instance attribute: width:
    * property def width(self): to retrieve it
    * property setter def width(self, value): to set it:
        * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
        * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
    * property def height(self): to retrieve it
    * property setter def height(self, value): to set it:
        * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
        * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter:
    * if width or height is equal to 0, perimeter has to be equal to 0
* print() and str() should print the rectangle with the character #: (see example below)
    * if width or height is equal to 0, return an empty string
* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x08$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/0x08$
```
**No test cases needed**
