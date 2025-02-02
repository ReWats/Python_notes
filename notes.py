# Syntax basics
# Python uses indentation to define code blocks

# Variables store data. Python automatically infers the type of variable

x = 5 #integer
name = "Alice"  #string

# PYTHON FUNCTIONS
# A Python finction is a block of reusable code that performs a specific task. Functions are defined using the def keyword.

# Defining a function

def greet(name):
    print("Hello, " + name + "!")

# def in the keyword to define a function
greet(name) :This is the function definition, where name is a parameter that wil be passed when calling the function.
# print() : This is the built-in Python finction to print text to the console.

# Calling a function
# To call the function and pass an argument:

greet("Alice")
# OUTPUT
# Hello, Alice

# Function with a return value
# A function can also return a value using the return keyword. This allows you to capture the result of the function in a variable.

def add(a, b):
  return a + b

result = add(3, 4)
print(result) # Output: 7

# Methods in Python
# A method is a function that is associated with an object. It is defined ubsaide a class and operates on the data contained in that class. You use methods to perform actions on an instance of the class.

#Example of a class and method"
class Person:
  def __init__(self, name, age):
    self.name = name
    sef.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

# Creating an instance of the Person class
person = Person("Alice", 25)
persom.greet() # calls the greet method

# self: In methods, self refers to the instance of the object. It allows access to the attributes and other methods in the class.
# init: The __init__ method is the constructor. It is automatically called when an object is created and is used to initialize object attributes

# Operators in Python
# Python provides several types of operators that you can use to perform operations on variables and values.

# a. Arithmetic Operators
#Used for mathematical operations.

x = 10
y = 5

print(x + y)  # Addition: 15
print(x - y)  # Subtraction: 5
print(x * y)  # Multiplication: 50
print(x / y)  # Division: 2.0
print(x // y) # Floor Division: 2 (rounds down the result)
print(x % y)  # Modulus (remainder): 0
print(x ** y) # Exponentiation: 100000

# Comparison Operators
# Used to compare values.

x = 10
y = 5

print(x == y)  # Equal to: False
print(x != y)  # Not equal to: True
print(x > y)   # Greater than: True
print(x < y)   # Less than: False
print(x >= y)  # Greater than or equal to: True
print(x <= y)  # Less than or equal to: False

# Logical Operators
# Used to combine conditional statements.

x = True
y = False

print(x and y)  # AND: False
print(x or y)   # OR: True
print(not x)    # NOT: False

# Assignment Operators
# Used to assign values to variables.

x = 5
x += 3  # x = x + 3
print(x)  # 8

x *= 2  # x = x * 2
print(x)  # 16

# Identity Operators
# Used to compare the memory locations of two objects.

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # True: both variables refer to the same object
print(x is z)  # False: x and z refer to different objects
print(x == z)  # True: x and z have the same content

# Membership Operators
# Used to test if a value is a member of a sequence (like a list or string).

x = [1, 2, 3, 4, 5]

print(3 in x)  # True: 3 is in the list
print(6 not in x)  # True: 6 is not in the list

# Control Flow: If, Elif, Else
# You can control the flow of your code using if, elif, and else.

x = 10

if x < 5:
    print("x is less than 5")
elif x == 10:
    print("x is 10")
else:
    print("x is greater than 5 but not 10")

# Loops: For and While
# For Loop
# The for loop is used to iterate over a sequence (like a list, tuple, string, or range).

for i in range(5):
    print(i)

# Output
0
1
2
3
4

# While Loop
# The while loop continues as long as a condition is True.

count = 0
while count < 5:
    print(count)
    count += 1
  
# Output 0
1
2
3
4

# List Comprehensions
# Python allows for compact loops to create lists, called list comprehensions.

squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Try and Except (Error Handling)
#Python uses try and except blocks to catch and handle exceptions (errors) that occur during the execution of code.

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Summary
# Functions are reusable blocks of code that perform specific tasks. They can accept parameters and return values.
# Methods are similar to functions but are associated with objects (instances of a class) and operate on their data.
# Operators are symbols that perform operations on variables and values, such as arithmetic, comparison, logical operations, and more.












