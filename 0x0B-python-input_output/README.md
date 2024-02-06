# 0x0B. Python - Input/Output

# Resources
**Read or watch**:

* 7.2. Reading and Writing Files
* 8.7. Predefined Clean-up Actions
* Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))
* JSON encoder and decoder
* Learn to Program 8 : Reading / Writing Files
* Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)
* All about py-file I/O

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
Why Python programming is awesome
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

# Python Test Cases
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* All your test files should be text files (extension: .txt)
* All your tests should be executed by using this command: python3 -m doctest ./tests/*
* All your modules should have a documentation (python3 -c 'print(\_\_import\_\_("my_module").\_\_doc\_\_)')
* All your classes should have a documentation (python3 -c 'print(\_\_import\_\_("my_module").MyClass.\_\_doc\_\_)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(\_\_import\_\_("my_module").my_function.\_\_doc\_\_)' and python3 -c 'print(\_\_import\_\_("my_module").MyClass.my_function.\_\_doc\_\_)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# Tasks
### 0. Read file - ([0-read_file.py]())
Write a function that reads a text file (UTF8) and prints it to stdout:

* Prototype: ```def read_file(filename=""):```
* You must use the ```with``` statement
* You don’t need to manage ```file permission``` or ```file doesn't exist``` exceptions.
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x0B$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

guillaume@ubuntu:~/0x0B$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ 
```
