name = "Beaux"
print(name.upper())  # this is an inline comment
print(type(name))  # this is a function to print the type of the variable

print(
    isinstance(name, str)
)  # this is a function to print the type of the variable to see if it is a string

age = float(3.9)  # this is a float

print(age)  # this is a float

print(isinstance(age, float))

age = 3, 2.5,  # This is a Tuple

print(age)

print(type(age))

print(
    isinstance(age, tuple)
)  # this is a function to print the type of the variable to see if it is a tuple

age = (20)  # this is an integer

print(
    isinstance(age, int)
)  # this is a function to print the type of the variable to see if it is an integer

#Arithmetic Operators
print(1 + 1)  # Addition
print(2 - 1)  # Subtraction
print(2 * 2)  # Multiplication
print(9 / 3)  # Division
print(5 % 2)  # Modulus
print(2**3)  # Exponentiation
print(5 // 2)  # Floor Division

age = 8
age += 8
print(age)  # age = age + 8

#Comparison Operators
a = 5
b = 10

print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to


#Ternary Operator, The Slower Way
def is_adult(age):
    if age > 18:
        return True
    else:
        return False  # This is a slower way to do it


#Ternary Operator, The Faster Way
def is_adult(age):
    return True if age > 18 else False  # This is a faster way to do it, which is called a ternary operator


#Strings
"Beau"  # This is a string
'Beau'  # This is a string
name = "Beau"  # This is a string
name += " is my name"  # This is a string concatenation
age = str(20)
print(name)
print("""Beau is 
20 years old""")

print("Beau".upper())
print("Beau".lower())
print("BEAU pERSon".title())
print("BEAU".islower())


def isalpha():
    """This is a function to check if the string contains only characters and is not empty"""
    pass


def isalnum():
    """This is a function to check if the string contains only characters and numbers (and is not empty)"""
    pass


def isdecimal():
    """This is a function to check if the string contains only decimal characters and is not empty"""
    pass


def lower():
    """This is a function to convert a string to lowercase"""
    pass


def islower():
    """This is a function to check if the string is in lowercase"""
    pass


def upper():
    """This is a function to convert a string to uppercase"""
    pass


def isupper():
    """This is a function to check if the string is in uppercase"""
    pass


def title():
    """This is a function to convert a string to title case"""
    pass


def startswith():
    """This is a function to check if the string starts with a specified value"""
    pass


def endswith():
    """This is a function to check if the string ends with a specified value"""
    pass


def replace():
    """This is a function to replace a specified value with another value in a string"""
    pass


def split():
    """This is a function to split a string into a list where each word is a list item"""
    pass


def strip():
    """This is a function to remove any whitespace from the beginning or the end of a string"""
    pass


def join():
    """This is a function to join a list into a string, with a specified separator between each item"""
    pass


def find():
    """This is a function to search for a specified value in a string and returns the position of where it was found"""
    pass


name = "Beau is my name"
print(name.lower())
print(len(name))
print(
    "au" in name
)  # This is a function to check if a string is in another string(Also called a substring)

#Escaping Characters
name = "Be\"lax"  # In this line we have a double quote inside a string
print(name)

name = 'Be"\"lax'  # In this line we have both a double quote in the middle of the string and a single quote outside the string
print(name)

name = 'Be\nau'  # \N = a newline character

print(name)

name = "Be\\au"  # In This line we have the second backslash, which is used to escape the first backslash so it prints out the name with the hasmark and not without the a like Beu.
print(name)

name = "Be\"aux\"au"  #This is a Hashmark comment for the term escaping, in this line we have a double quote inside a string

print(name.upper())  # this is an inline comment

# String Characaters And Slicing
name = 'Beau is cool'
print(name[-4:9]
      )  # This is a function to print the first character of the string
#Strings are false only if they are empty

#Booleans
done = True  # This is a boolean variable. it defines any value as the chance to be true if it is either a number or a character otherwise if it says nothing like 0 or an empty string it will be false
print(type(done) == bool)
if done:
    print("Yes, it is done")
else:
    print("No, it is not done")

book_1_read = True
book_2_read = False

read_any_book = any([
    book_1_read, book_2_read
])  # This is a function to check if any of the variables are true

ingredients_purchased = True
meals_cooked = False

ready_to_serve = all([ingredients_purchased, meals_cooked])

#Number Data Types

num1 = 2 + 3j  # This is a complex number
num2 = complex(2, 3)  # This is a complex number
print(
    num2.real, num2.imag
)  # This is a function to print the real and imaginary parts of a complex number

# Built in Functions
print(round(5.445,
            2))  # This is a function to round a number to the nearest integer

#Enums - These are readable names bound to a constant value. Enums are great for things that you know aren't going to change, like months, days, colors, etc.

from enum import Enum


class Stat(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(Stat.ACTIVE)
